from datetime import datetime
import os
class FileOperator:
    print("Welcome to Personal Journal Manager!")

    def add_entry(self):
        current_date_time=datetime.now()
        c=current_date_time.strftime("%d-%m-%Y %H:%M:%S")
        f=open("data.txt",'a')
        entry=input("Enter your journal entry:\n")
        f.write(f"{c}")
        f.write("\n")
        f.write(f"{entry}")
        f.write("\n")
        f.close()
        print("\nEntry added successfully!")
    
    def view_entries(self):
        try:
            f=open("data.txt",'r')
            print("\nYour journal entries:")
            print("-"*20)
            for i in f.readlines():
                print(i)
            f.close()
        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")
    
    def search_entry(self):
        try:
            f=open("data.txt")
            keyword=input("\nEnter the keyword or date to search:")
            is_found=0
            entry=None
            for i in f.readlines():
                if keyword in i:
                    is_found=1
                    entry=i
                else:
                    continue
                
            if is_found!=0:
                print("Matching Entries:")
                print("-"*10)
                print(entry)
        
            if is_found==0:
                print(f"\nNo entries were found for the keyword: {keyword}")
        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")
    
    def delete_entries(self):
        try:
            choice=input("\nAre you sure you want to delete all entries? (yes/no):")
            if choice=="yes":
                os.remove("C:\development\python\Project-7\data.txt")
                print("\nAll journal entries have been deleted.")
        except FileNotFoundError:
            print("\nNo journal entries to delete.")
    
    def ask_user(self):
        while True:
            print("\nPlease select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")
            choice=int(input("\nUser Input:"))
            
            if choice==1:
                self.add_entry()
            elif choice==2:
                self.view_entries()
            elif choice==3:
                self.search_entry()
            elif choice==4:
                self.delete_entries()
            elif choice==5:
                break
            else:
                print("\nInvalid choice!")

obj=FileOperator()
obj.ask_user()