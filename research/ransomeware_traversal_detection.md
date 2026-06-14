# Research on Ransomware Traversal Techniques

## Objective

To understand how modern ransomware traverses directories and identifies target files before encryption.

---

# Key Findings

## Recursive Directory Traversal

Most ransomware variants recursively scan folders to locate sensitive user files.

Common target directories:

* Documents
* Desktop
* Downloads
* Pictures
* Shared drives

---

## File Extension Filtering

Ransomware targets valuable file types such as:

* .docx
* .xlsx
* .pdf
* .jpg
* .png
* .db

System-critical files are often skipped to prevent system crashes before ransom delivery.

---

## Multithreaded Encryption

Modern ransomware frequently uses parallel processing techniques to encrypt files rapidly and avoid detection.

---

## Behavioral Characteristics

Common ransomware behaviors include:

* rapid folder traversal
* high file access frequency
* mass rename operations
* unusual disk activity

---

# Proposed Detection Strategy

The project proposes an early-stage detection model based on:

* distributed honeyfiles
* traversal monitoring
* behavioral analysis
* AI-based threat scoring

The goal is to identify ransomware activity before large-scale encryption occurs.
