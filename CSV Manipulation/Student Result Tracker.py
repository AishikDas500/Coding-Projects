import pandas as pd 

file_name = input("Enter file path: ").strip().strip('"')

try:
    marksheet = pd.read_csv(file_name)
except Exception as e:
    print("Error while reading the document")
    quit()
marks_list = {}
while True:
    try: 
        n = int(input("Enter number of students who marks you want to add in the new CSV: "))
        break
    except:
        print("Please select a number")
        continue
def get_student_result(roll_no):
    # Match roll numbers whether they are int or string (handles stray spaces)
    marks = marksheet["Roll No."].astype(str).str.strip() == str(roll_no).strip()  # Converts everyting into string and removes any spaces then checks with thue user input 
    result = marksheet[marks]
    if not result.empty:
        return result
    # return empty DataFrame (caller already checks for missing roll numbers)
    return pd.DataFrame(columns=marksheet.columns)
for j in range(n):
    roll_no = int(input("Enter Roll Number of the student: "))
    if roll_no not in marksheet["Roll No."].values:
        print("Roll Number not found.")
        continue
    else:
        for i in get_student_result(roll_no).values:
            name = i[1]
            m1 = i[2]
            m2 = i[3]
            m3 = i[4]
            m4 = i[5]
            m5 = i[6]
            m6 = i[7]   
        
        
        li = [m1 , m2 , m3 , m4 , m5 , m6]
        total = sum(li)
        p_5 = ((total - m6) / 500) * 100 #OG 5 
        p_6 = (total/ 600 ) * 100  # all 6
        p_b = ((total - min(li)) / 500 ) * 100 #best 5 
        data = [name, total, round(p_5 , 2), round(p_6, 2), round(p_b, 2)]
    marks_list[roll_no] = data
    marks = marksheet["Roll No."].astype(str).str.strip() == str(roll_no).strip()
    marksheet.loc[marks, "Total Marks"] = total
    marksheet.loc[marks, "Top 5 Percentage"] = round(p_5, 2)
    marksheet.loc[marks, "All 6 Precentage"] = round(p_6, 2)
    marksheet.loc[marks, "Best 5 Precentage"] = round(p_b, 2)
    marksheet.loc[marks, "Report"] = str(data)

print(marks_list)
user_choice = input("Do you want to add these datas of the following students in a new CSV file (Y/N)? ").lower()
if user_choice == "y" or "yes":
    new_file_name = input("Enter file name: ").strip() + ".csv"
    marksheet.to_csv(new_file_name, index = False)
else:
    quit()