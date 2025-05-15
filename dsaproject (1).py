class Equipment:
    class Node:
        def __init__(self, equipment_name, quantity):
            self.equipment_name = equipment_name
            self.quantity = quantity
            self.next = None

    def __init__(self):
        self.head = None
        self.sz = 0

    def add_equipment(self, equipment_name, quantity):
        new = self.Node(equipment_name, quantity)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
        self.sz += 1

    def print_equipment(self):
        tnode = self.head
        while tnode is not None:
            print(f"{tnode.equipment_name}: {tnode.quantity}")
            tnode = tnode.next


class Pharmacy:
    class Node:
        def __init__(self, medicine_name, quantity):
            self.medicine_name = medicine_name
            self.quantity = quantity
            self.next = None

    def __init__(self):
        self.head = None
        self.sz = 0

    def add_medicine(self, medicine_name, quantity):
        new = self.Node(medicine_name, quantity)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
        self.sz += 1

    def print_medicines(self):
        tnode = self.head
        while tnode is not None:
            print(f"{tnode.medicine_name}: {tnode.quantity}")
            tnode = tnode.next


class Graph:
    class Node:
        def __init__(self, data):
            self.data = data
            self.neighbors = []

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        if data not in self.vertices:
            self.vertices[data] = self.Node(data)

    def add_edge(self, data1, data2):
        if data1 in self.vertices and data2 in self.vertices:
            self.vertices[data1].neighbors.append(data2)
            self.vertices[data2].neighbors.append(data1)

    def display_graph(self):
        for vertex in self.vertices:
            print(vertex, "->", self.vertices[vertex].neighbors)


class Patients:
    class Node:
        def __init__(self, name, age, problem, timing, k, condition):
            self.patient_name = name
            self.age = age
            self.problem = problem
            self.timing = timing
            self.condition = condition
            self.assigned_doctor = k
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
        self.max = 0

    def add_patient(self, name, age, problem, timing, k, condition):
        new = self.Node(name, age, problem, timing, k, condition)
        if condition == "normal":
            if self.sz == 0:
                self.front = self.rear = new
            else:
                current = self.front
                previous = None
                while current is not None:
                    if current.timing > timing:
                        break
                    if current.timing == timing:
                        print("Patient is already allotted. Please, change your time.")
                        timing = int(input("Enter the time: "))
                    previous = current
                    current = current.next
                if previous is None:
                    new.next = self.front
                    self.front = new
                else:
                    previous.next = new
                    new.next = current
                    if current is None:
                        self.rear = new
        elif condition == "emergency":
            if self.sz == 0:
                self.front = self.rear = new
            else:
                new.next = self.front
                self.front = new
        self.sz += 1
        self.max = self.sz

    def delete_patient(self, patient_name):
        if self.sz == 0:
            print("No patients in the list.")
            return
        elif self.sz == 1:
            if self.front.patient_name == patient_name:
                print(patient_name, "deleted.")
                self.front = self.rear = None
                self.sz -= 1
            else:
                print("Patient not found in the list.")
            return

        prev_node = None
        curr_node = self.front

        while curr_node is not None and curr_node.patient_name != patient_name:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            print("Patient not found in the list.")
            return

        if prev_node is not None:
            prev_node.next = curr_node.next
            if curr_node == self.rear:
                self.rear = prev_node
            print(patient_name, "deleted.")
            self.sz -= 1
        else:
            self.front = curr_node.next
            if self.sz == self.max:
                self.max -= 1
            print(patient_name, "deleted.")
            self.sz -= 1


class Staff:
    class Node:
        def __init__(self, name, specialization, start, end):
            self.doctor_name = name
            self.specialization = specialization
            self.start = start
            self.end = end
            self.next = None

    def __init__(self):
        self.head = None
        self.sz = 0

    def add_staff(self, name, specialization, start, end):
        new = self.Node(name, specialization, start, end)
        if self.sz == 0:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
        self.sz += 1

    def print_doctors(self):
        tnode = self.head
        while tnode is not None:
            print(tnode.doctor_name, end=" ")
            tnode = tnode.next
        print("")


class HospitalAttributes:
    class Node:
        def __init__(self, name):
            self.attribute_name = name
            self.doctors = Staff()
            self.patients = Patients()
            self.equipment = Equipment()
            self.pharmacy = Pharmacy()  # Added pharmacy attribute
            self.next = None

    def __init__(self):
        self.head = None
        self.sz = 0

    def set_attributes(self):
        while True:
            if self.sz == 0:
                new = self.Node("doctor")
                self.head = new
                self.sz += 1
            elif self.sz == 1:
                new = self.Node("patients")
                new.next = self.head
                self.head = new
                self.sz += 1
            elif self.sz == 2:
                new = self.Node("consultation")
                new.next = self.head
                self.head = new
                self.sz += 1
            elif self.sz == 3:
                new = self.Node("equipment")
                new.next = self.head
                self.head = new
                self.sz += 1
            elif self.sz == 4:
                new = self.Node("pharmacy")
                new.next = self.head
                self.head = new
                self.sz += 1
            else:
                break

    def add_members(self, name):
        start = self.head
        while start is not None:
            if name == start.attribute_name:
                if name == "doctor":
                    name = input("Doctor name: ")
                    specialization = input("specialization: ")
                    start_time = int(input("Starting time: "))
                    ending_time = int(input("Ending time: "))
                    start.doctors.add_staff(name, specialization, start_time, ending_time)
                    start.doctors.print_doctors()
                    break
                elif name == "patients":
                    name = input("Patient name: ")
                    problem = input("Problem: ")
                    timing = int(input("Timing: "))
                    age = int(input("Age: "))
                    condition = input("Condition (normal/emergency): ")
                    k = self.assign_doctor(start, problem, timing)
                    if k is not None:
                        start.patients.add_patient(name, age, problem, timing, k, condition)
                        start.patients.print_patients()
                    break
                elif name == "consultation":
                    self.consulting(start)
                    break
                elif name == "equipment":
                    self.add_equipment(start)
                    break
                elif name == "pharmacy":
                    self.add_medicine(start)
                    break
                else:
                    break
            start = start.next

    def assign_doctor(self, start, problem, timing):
        doctor_node = start.next
        flag = 0
        while doctor_node is not None:
            doctor = doctor_node.doctors.head
            while doctor is not None:
                if doctor.specialization.lower() == problem.lower():
                    flag = 1
                    if doctor.start <= timing <= doctor.end:
                        flag = 2
                        break
                doctor = doctor.next
            if flag == 2:
                return doctor.doctor_name
            elif flag == 1:
                print("Doctor with specialization '{}' is not available at that particular time.".format(problem))
            elif flag == 0:
                print("No doctor available to treat the disease '{}'.".format(problem))
            doctor_node = doctor_node.next
        return None

    def consulting(self, start):
        doctor_node = start.next.next
        patient_node = start.next
        doctor = doctor_node.doctors.head
        patient_list = []
        i = 0
        while doctor is not None:
            patient_list.append([])
            curnode = patient_node.patients.front
            while curnode is not None:
                if doctor.doctor_name == curnode.assigned_doctor:
                    patient_list[i].append(curnode.patient_name)
                curnode = curnode.next
            doctor = doctor.next
            i += 1
        j = i
        for k in range(j):
            for a in patient_list[k]:
                patient_node.patients.delete_patient(a)

    def add_equipment(self, start):
        equipment_name = input("Enter equipment name: ")
        quantity = int(input("Enter quantity: "))
        start.equipment.add_equipment(equipment_name, quantity)
        start.equipment.print_equipment()

    def add_medicine(self, start):
        medicine_name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity: "))
        start.pharmacy.add_medicine(medicine_name, quantity)
        start.pharmacy.print_medicines()


def main():
    h = HospitalAttributes()
    h.set_attributes()
    print("a) To add new doctors")
    print("b) To add new patients")
    print("c) Patient consulting the doctor")
    print("d) Add equipment")
    print("e) Add medicine to the pharmacy")
    while True:
        choice = input("Enter the choice:")
        if choice == "a":
            name = "doctor"
            h.add_members(name)
        elif choice == "b":
            name = "patients"
            h.add_members(name)
        elif choice == "c":
            name = "consultation"
            h.consulting(h.head)
        elif choice == "d":
            name = "equipment"
            h.add_members(name)
        elif choice == "e":
            name = "pharmacy"
            h.add_members(name)
        else:
            break


if __name__ == "__main__":
    main()
