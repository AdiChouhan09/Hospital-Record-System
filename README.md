# Hospital Patient Record Management System

---

## Overview

The **Hospital Patient Record Management System (HPRMS)** is a conceptual software solution designed to simulate how hospitals manage patient records, emergency workflows, billing operations, and basic inventory.  
This assignment applies **linear data structures** linked lists, stacks, and queues to model real-world healthcare processes and to understand how data structure choices impact efficiency and system performance.

---

## Objectives

- Implement a simplified hospital management model using core data structures.
- Use linked lists, queues, and stacks to simulate patient admission, emergency triage, billing, and inventory operations.
- Develop modular design thinking and structured problem-solving.
- Strengthen theoretical understanding of linear data structures through applied use-cases.
- Demonstrate complexity analysis for each implemented operation.
- Build a clean, menu-driven system showcasing different management workflows.

---

## Data Structures Used

### **1. Linked List**
Used for:
- Patient master records  
- Inventory management  

**Reason:**  
Allows dynamic addition, deletion, and traversal of records without memory reallocation.

---

### **2. Queue**
Used for:
- Patient admission queues (OPD/IPD)
- Emergency case handling (optional: priority enhancements)

**Reason:**  
Follows **FIFO**, ideal for real-world hospital queues where patients are processed in order of arrival.

---

### **3. Stack**
Used for:
- Billing history tracking  
- Undo operations in billing  
- Change history for patient records  

**Reason:**  
Follows **LIFO**, enabling easy rollback of the most recent actions.

---

## Functionalities

### **1. Patient Management Module**
- Add patient  
- Update patient details  
- Delete patient  
- Search patient (ID, name, date)  
- Discharge & generate report  

---

### **2. Emergency Management Module**
- Add emergency case  
- Display emergency queue  
- Pop highest-priority case for treatment  

---

### **3. Billing System**
- Add billable items (lab tests, room charges, medicines, procedures)  
- Auto-calculate totals and taxes  
- Undo last billing action using stack  
- Final bill generation  

---

### **4. Inventory Management**
- Add inventory item  
- Update stock  
- Search item  
- Low-stock alerts  

---

## Implementation Steps

### **Step 1 — Define System Nodes & Structures**
- Create patient node structure  
- Create inventory item structure  
- Create linked list, stack, and queue classes  

### **Step 2 — Implement Core Data Structure Operations**
- Linked list: insert, delete, update, search  
- Queue: enqueue, dequeue, peek  
- Stack: push, pop, top  

### **Step 3 — Develop Modules**
- Patient Management functions  
- Emergency Queue functions  
- Billing functions  
- Inventory functions  

### **Step 4 — Integrate With Menu-Driven Program**
Example:
- Patient Management
- Emergency Queue
- Billing
- Inventory
- Exit


### **Step 5 — Testing**
- Add test data  
- Validate queue order logic  
- Validate undo operation via stack  
- Ensure linked list CRUD works as expected  

### **Step 6 — Complexity Documentation**
Include complexity for:
- Insertions  
- Deletions  
- Queue operations  
- Stack operations  

---

## Technologies 

- Python 3  
- Object-Oriented Programming
- Data Structures (Linked List, Stack, Queue)   

---

## Learning Outcomes

By completing this assignment, you will learn to:

- Apply theoretical data structures to real-world-style hospital management.
- Understand operational flows for admissions, billing, emergencies, and inventory.
- Implement stacks, queues, and linked lists from scratch.
- Structure a modular software solution.
- Analyse time and space complexity for linear data structures.
- Build error-free menu-driven programs.
- Document software systems professionally (GitHub-standard README).

---

## Author

**Name:** Aditya Chouhan  
**Roll No:** 2401830001  
**Course:** B.Sc. (H) Cybersecurity  

---


