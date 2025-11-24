class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_predicate(self, predicate):
        prev = None
        curr = self.head
        while curr:
            if predicate(curr.data):
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return curr.data
            prev = curr
            curr = curr.next
        return None

    def find(self, predicate):
        temp = self.head
        while temp:
            if predicate(temp.data):
                return temp.data
            temp = temp.next
        return None

    def traverse(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

class EmergencyCase:
    def __init__(self, patient, severity, arrival_index):
        self.patient = patient
        self.severity = severity
        self.arrival_index = arrival_index

class EmergencyQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, emergency_case):
        node = Node(emergency_case)
        if self.head is None:
            self.head = node
            return
        if self._higher_priority(emergency_case, self.head.data):
            node.next = self.head
            self.head = node
            return
        prev = None
        curr = self.head
        while curr and not self._higher_priority(emergency_case, curr.data):
            prev = curr
            curr = curr.next
        prev.next = node
        node.next = curr

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def traverse(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next

    @staticmethod
    def _higher_priority(a, b):
        if a.severity > b.severity:
            return True
        if a.severity == b.severity:
            return a.arrival_index < b.arrival_index
        return False

class Patient:
    def __init__(self, pid, name, age, gender, diagnosis, admission_type):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.admission_type = admission_type

    def __str__(self):
        return f"[ID: {self.pid}] {self.name}, Age: {self.age}, Gender: {self.gender}, Type: {self.admission_type}, Diagnosis: {self.diagnosis}"

class InventoryItem:
    def __init__(self, item_id, name, quantity, unit_price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"[Item ID: {self.item_id}] {self.name} | Qty: {self.quantity} | Unit Price: {self.unit_price}"

class BillItem:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: {self.amount:.2f} INR"

class Bill:
    def __init__(self, patient):
        self.patient = patient
        self.items = []
        self.history = Stack()

    def add_item(self, description, amount):
        item = BillItem(description, amount)
        self.items.append(item)
        self.history.push(("add", item))

    def undo_last_action(self):
        action = self.history.pop()
        if action is None:
            print("No billing actions to undo.")
            return
        t, item = action
        if t == "add":
            for i in range(len(self.items) - 1, -1, -1):
                if self.items[i] is item:
                    del self.items[i]
                    break
            print("Last billing item removed.")

    def total_amount(self):
        return sum(i.amount for i in self.items)

    def print_bill(self):
        print("\n===== BILL SUMMARY =====")
        print(self.patient)
        print("-------------------------")
        if not self.items:
            print("No billable items added yet.")
        else:
            for i in self.items:
                print(" -", i)
            print("-------------------------")
            print(f"Total: {self.total_amount():.2f} INR")
        print("=========================\n")

class HospitalSystem:
    def __init__(self):
        self.patients = LinkedList()
        self.inventory = LinkedList()
        self.emergency_queue = EmergencyQueue()
        self.next_patient_id = 1
        self.next_item_id = 1
        self.emergency_arrival_counter = 0

    def add_patient(self):
        print("\n--- Add Patient ---")
        name = input("Name: ").strip()
        age = self._read_int("Age: ")
        gender = input("Gender (M/F/O): ").strip()
        diagnosis = input("Diagnosis: ").strip()
        admission_type = input("Admission Type (OPD/IPD/Emergency): ").strip().upper()
        pid = self.next_patient_id
        self.next_patient_id += 1
        patient = Patient(pid, name, age, gender, diagnosis, admission_type)
        self.patients.append(patient)
        print(f"Patient added with ID: {pid}")
        if admission_type == "EMERGENCY":
            self._add_to_emergency_queue(patient)

    def view_patients(self):
        print("\n--- Patient List ---")
        found = False
        for p in self.patients.traverse():
            print(p)
            found = True
        if not found:
            print("No patients found.")

    def search_patient(self):
        print("\n--- Search Patient ---")
        pid = self._read_int("Enter Patient ID: ")
        p = self.patients.find(lambda x: x.pid == pid)
        if p:
            print("Patient found:")
            print(p)
        else:
            print("Patient not found.")

    def update_patient(self):
        print("\n--- Update Patient ---")
        pid = self._read_int("Enter Patient ID: ")
        p = self.patients.find(lambda x: x.pid == pid)
        if not p:
            print("Patient not found.")
            return
        print("Leave blank to keep existing.")
        n = input(f"Name [{p.name}]: ").strip()
        a = input(f"Age [{p.age}]: ").strip()
        g = input(f"Gender [{p.gender}]: ").strip()
        d = input(f"Diagnosis [{p.diagnosis}]: ").strip()
        t = input(f"Admission Type [{p.admission_type}]: ").strip()
        if n: p.name = n
        if a:
            try: p.age = int(a)
            except: pass
        if g: p.gender = g
        if d: p.diagnosis = d
        if t: p.admission_type = t.upper()
        print("Patient updated.")

    def discharge_patient(self):
        print("\n--- Discharge Patient ---")
        pid = self._read_int("Enter Patient ID: ")
        removed = self.patients.delete_by_predicate(lambda x: x.pid == pid)
        if removed:
            print("Patient discharged:")
            print(removed)
        else:
            print("Patient not found.")

    def _add_to_emergency_queue(self, patient):
        print("Emergency details:")
        sev = self._read_int("Severity (1-5): ", 1, 5)
        self.emergency_arrival_counter += 1
        case = EmergencyCase(patient, sev, self.emergency_arrival_counter)
        self.emergency_queue.enqueue(case)
        print("Emergency case added.")

    def add_emergency_case(self):
        print("\n--- Add Emergency Case ---")
        c = input("Already registered? (Y/N): ").strip().upper()
        if c == "Y":
            pid = self._read_int("Patient ID: ")
            p = self.patients.find(lambda x: x.pid == pid)
            if not p:
                print("Patient not found.")
                return
        else:
            name = input("Name: ").strip()
            age = self._read_int("Age: ")
            gender = input("Gender (M/F/O): ").strip()
            diag = input("Diagnosis: ").strip()
            pid = self.next_patient_id
            self.next_patient_id += 1
            p = Patient(pid, name, age, gender, diag, "EMERGENCY")
            self.patients.append(p)
            print(f"Emergency patient registered with ID: {pid}")
        self._add_to_emergency_queue(p)

    def view_emergency_queue(self):
        print("\n--- Emergency Queue ---")
        f = False
        for case in self.emergency_queue.traverse():
            print(f"Severity: {case.severity} | Arrival: {case.arrival_index} | {case.patient}")
            f = True
        if not f:
            print("Queue empty.")

    def treat_next_emergency(self):
        print("\n--- Treat Next Emergency ---")
        case = self.emergency_queue.dequeue()
        if not case:
            print("No cases.")
        else:
            print(f"Treating: Severity {case.severity} | {case.patient}")

    def billing_menu(self):
        print("\n--- Billing ---")
        pid = self._read_int("Patient ID: ")
        p = self.patients.find(lambda x: x.pid == pid)
        if not p:
            print("Patient not found.")
            return
        bill = Bill(p)
        while True:
            print("\n1. Add item\n2. Undo\n3. Show bill\n4. Close")
            c = input("Choose: ").strip()
            if c == "1":
                desc = input("Description: ").strip()
                amt = self._read_float("Amount: ")
                bill.add_item(desc, amt)
                print("Added.")
            elif c == "2":
                bill.undo_last_action()
            elif c == "3":
                bill.print_bill()
            elif c == "4":
                bill.print_bill()
                break

    def add_inventory_item(self):
        print("\n--- Add Inventory Item ---")
        name = input("Item name: ").strip()
        qty = self._read_int("Quantity: ", 0)
        price = self._read_float("Unit price: ", 0)
        item_id = self.next_item_id
        self.next_item_id += 1
        item = InventoryItem(item_id, name, qty, price)
        self.inventory.append(item)
        print(f"Item added with ID: {item_id}")

    def view_inventory(self):
        print("\n--- Inventory ---")
        f = False
        for i in self.inventory.traverse():
            print(i)
            f = True
        if not f:
            print("No items.")

    def update_inventory_stock(self):
        print("\n--- Update Stock ---")
        iid = self._read_int("Item ID: ")
        item = self.inventory.find(lambda x: x.item_id == iid)
        if not item:
            print("Item not found.")
            return
        print("Current:", item)
        delta = self._read_int("Change (+/-): ")
        item.quantity += delta
        if item.quantity < 0:
            item.quantity = 0
        print("Updated:", item)

    def low_stock_report(self):
        print("\n--- Low Stock ---")
        th = self._read_int("Threshold: ", 0)
        f = False
        for i in self.inventory.traverse():
            if i.quantity <= th:
                print(i)
                f = True
        if not f:
            print("No low stock.")

    @staticmethod
    def _read_int(prompt, minimum=None, maximum=None):
        while True:
            try:
                v = int(input(prompt))
                if minimum is not None and v < minimum:
                    continue
                if maximum is not None and v > maximum:
                    continue
                return v
            except:
                pass

    @staticmethod
    def _read_float(prompt, minimum=None):
        while True:
            try:
                v = float(input(prompt))
                if minimum is not None and v < minimum:
                    continue
                return v
            except:
                pass

def main():
    sys = HospitalSystem()
    while True:
        print("\n========== HPRMS ==========")
        print("1. Patient Management")
        print("2. Emergency Queue")
        print("3. Billing")
        print("4. Inventory")
        print("5. Exit")
        c = input("Select: ").strip()

        if c == "1":
            while True:
                print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Discharge\n6. Back")
                s = input("Select: ").strip()
                if s == "1":
                    sys.add_patient()
                elif s == "2":
                    sys.view_patients()
                elif s == "3":
                    sys.search_patient()
                elif s == "4":
                    sys.update_patient()
                elif s == "5":
                    sys.discharge_patient()
                elif s == "6":
                    break

        elif c == "2":
            while True:
                print("\n1. Add Emergency\n2. View Queue\n3. Treat\n4. Back")
                s = input("Select: ").strip()
                if s == "1":
                    sys.add_emergency_case()
                elif s == "2":
                    sys.view_emergency_queue()
                elif s == "3":
                    sys.treat_next_emergency()
                elif s == "4":
                    break

        elif c == "3":
            sys.billing_menu()

        elif c == "4":
            while True:
                print("\n1. Add Item\n2. View Items\n3. Update Stock\n4. Low Stock Report\n5. Back")
                s = input("Select: ").strip()
                if s == "1":
                    sys.add_inventory_item()
                elif s == "2":
                    sys.view_inventory()
                elif s == "3":
                    sys.update_inventory_stock()
                elif s == "4":
                    sys.low_stock_report()
                elif s == "5":
                    break

        elif c == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
