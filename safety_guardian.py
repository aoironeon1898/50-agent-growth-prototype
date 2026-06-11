"""safety_guardian.py - Enforce safety constraints on growth"""

import time
import os
from pathlib import Path

class SafetyGuardian:
    """Enforce hard limits and safety checks."""
    
    def __init__(self, max_disk_mb=100, max_runtime_sec=300, max_files=1000):
        self.max_disk_mb = max_disk_mb
        self.max_runtime_sec = max_runtime_sec
        self.max_files = max_files
        self.start_time = None
        self.violations = []

    def start_session(self):
        """Mark start of growth session."""
        self.start_time = time.time()
        self.violations = []

    def check_runtime(self):
        """Check if runtime exceeded."""
        if not self.start_time:
            return True
        elapsed = time.time() - self.start_time
        if elapsed > self.max_runtime_sec:
            self.violations.append(f"Runtime exceeded: {elapsed}s > {self.max_runtime_sec}s")
            return False
        return True

    def check_disk_usage(self, skill_dir):
        """Check disk usage in skill directory."""
        try:
            total_size = sum(f.stat().st_size for f in Path(skill_dir).rglob('*'))
            size_mb = total_size / (1024 * 1024)
            if size_mb > self.max_disk_mb:
                self.violations.append(f"Disk usage exceeded: {size_mb:.1f}MB > {self.max_disk_mb}MB")
                return False
        except Exception as e:
            self.violations.append(f"Disk check failed: {e}")
        return True

    def check_file_count(self, skill_dir):
        """Check number of skill files."""
        try:
            count = len(list(Path(skill_dir).glob('skill_*.py')))
            if count > self.max_files:
                self.violations.append(f"Too many files: {count} > {self.max_files}")
                return False
        except Exception as e:
            self.violations.append(f"File count check failed: {e}")
        return True

    def can_proceed(self, skill_dir):
        """Check all safety constraints."""
        return (self.check_runtime() and 
                self.check_disk_usage(skill_dir) and 
                self.check_file_count(skill_dir))

    def get_violations(self):
        """Return list of violations."""
        return self.violations

class RateLimiter:
    """Rate limit growth to prevent runaway expansion."""
    
    def __init__(self, max_per_minute=60, max_per_hour=1000):
        self.max_per_minute = max_per_minute
        self.max_per_hour = max_per_hour
        self.creation_times = []

    def can_create(self):
        """Check if creation is allowed."""
        now = time.time()
        minute_ago = now - 60
        hour_ago = now - 3600
        
        self.creation_times = [t for t in self.creation_times if t > hour_ago]
        
        minute_count = len([t for t in self.creation_times if t > minute_ago])
        hour_count = len(self.creation_times)
        
        if minute_count >= self.max_per_minute:
            return False, f"Rate limit (per minute): {minute_count}/{self.max_per_minute}"
        if hour_count >= self.max_per_hour:
            return False, f"Rate limit (per hour): {hour_count}/{self.max_per_hour}"
        
        return True, "OK"

    def record_creation(self):
        """Record a skill creation."""
        self.creation_times.append(time.time())
