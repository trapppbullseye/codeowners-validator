#!/usr/bin/env python3
"""Validate CODEOWNERS file syntax"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Validate CODEOWNERS file syntax")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("codeowners-validator v0.1.0");return
 print(f"[12:00] codeowners-validator ready")
if __name__=="__main__":main()
