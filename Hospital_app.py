class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Drug:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

    def __str__(self):
        return f"Name: {self.name}\nDosage: {self.dosage}"


class HospitalApp:
    def __init__(self):
        self.users = []
        self.patients = []
        self.drugs = []
        self.logged_in = False
        self.current_user = None

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = User(username, password)
        self.users.append(user)
        print("User registered successfully.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in = True
                self.current_user = user
                print("Login successful.")
                return

        print("Invalid username or password.")

    def logout(self):
        self.logged_in = False
        self.current_user = None
        print("Logged out successfully.")

    def add_patient(self):
        if not self.logged_in:
            print("Please log in to add a patient.")
            return

        name = input("Enter patient's name: ")
        age = input("Enter patient's age: ")
        condition = input("Enter patient's condition: ")

        patient = Patient(name, age, condition)
        self.patients.append(patient)
        print("Patient added successfully.")

    def view_patients(self):
        if len(self.patients) == 0:
            print("No patients registered.")
        else:
            for i, patient in enumerate(self.patients, start=1):
                print(f"\nPatient {i}")
                print(patient)

    def add_drug(self):
        if not self.logged_in:
            print("Please log in to add a drug.")
            return

        name = input("Enter drug's name: ")
        dosage = input("Enter drug's dosage: ")

        drug = Drug(name, dosage)
        self.drugs.append(drug)
        print("Drug added successfully.")

    def view_drugs(self):
        if len(self.drugs) == 0:
            print("No drugs available.")
        else:
            for i, drug in enumerate(self.drugs, start=1):
                print(f"\nDrug {i}")
                print(drug)

    def run(self):
        while True:
            print("\n===== Hospital App Menu =====")
            print("1. Register user")
            print("2. Login")
            print("3. Logout")
            print("4. Add patient")
            print("5. View patients")
            print("6. Add drug")
            print("7. View drugs")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.logout()
            elif choice == "4":
                self.add_patient()
            elif choice == "5":
                self.view_patients()
            elif choice == "6":
                self.add_drug()
            elif choice == "7":
                self.view_drugs()
            elif choice == "8":
                print("Exiting the Hospital App.")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate and run the app
app = HospitalApp()
app.run()

