from datetime import datetime
from itertools import count
from typing import Dict, Any, final

class User:
    def __init__(self, fullname: str, email: str, _passwrd: str) -> None:
        self.fullname: str = fullname
        self._passwrd: str = _passwrd
        self.email = email
        self._date_joined = datetime.now()
        

    def __repr__(self) -> str:
        return f"Class <User>"
    def __str__(self) -> str:
        return f"Full Name: {self.fullname} Email: {self.email}"
    
    def change_passwrd(self, _oldpasswrd: str, _newpasswrd) -> str:
        if(_oldpasswrd == self._passwrd):
            self._passwrd = _newpasswrd
            return f"Password Changed Successfully!!!"
        else:
            return f"Wrong Password. Please type your current Password correctly to change the password."
        

    
    @property
    def _get_joining_date(self) -> str:
        return f"{self._date_joined.strftime('%B %d, %Y')}"
    
@final  
class Student(User):
    _sr_counter = count(start=1)
    def __init__(self, fullname: str, email: str, _passwrd: str, animation_Type: str, software: str, lang: str, auto_Earn: bool, kiosk: bool, edu_email: str) -> None:
    
        super().__init__(fullname, email, _passwrd)
        self.sr_no: int = next(Student._sr_counter)
        self.animation_Type = animation_Type
        self.software = software
        self.lang = lang
        self.auto_Earn = auto_Earn
        self.kiosk = kiosk
        self.edu_email = edu_email
        self.LMS_id: str= "None"
        self._mycourses: Dict[int, Dict[str, Any]] = {}

    @property
    def mycourses_summary(self)->str:
        if not self._mycourses:
            return f'No course currently Enrolled'
        else:
            all_courses: str =""
            for cid, data in self._mycourses.items():
                all_courses += f"Course Id: {cid}\nProgress: {data["progress"]}\nHours Leared: {data["hours"]}\nCompleted Lessons: {data['completed_lessons']}\nAchievements: {data['achievements']}\n\n"
            return f"{all_courses}"
            
    def mycourse_summary(self, courseId) -> str:
        if courseId not in self._mycourses.keys():
            return f"This course doesn't exist in the user enrolled courses."
        else:
            data = self._mycourses[courseId]
            return f"Course Id: {courseId}\nProgress: {data["progress"]}\nHours Leared: {data["hours"]}\nCompleted Lessons: {data['completed_lessons']}\nAchievements: {data['achievements']}"

    
    def enroll_course(self, courseId) -> str:
        if courseId in self._mycourses.keys():
            return f"Course Already enrolled by the user."
        self._mycourses[courseId] = {
            "progress": 0.0,           # percent 0.0–100.0
            "hours": 0.0,
            "completed_lessons": 0,
            "achievements": 0
        }
        return f"Course {courseId} Enrolled Successfully!!!!"

        

    def updateprogress(self, courseId: int, updated_progress: float)-> str:
        course = self._mycourses[courseId]
        if course is None:
            return f"Course not found..."
        else:
            course['progress'] = max(0.0, (min(100, float(updated_progress))))
            return f"Course Progress Updated!!!"

    def updatehours(self, courseId: int, hours: float)-> str:
        course = self._mycourses[courseId]
        if course is None:
            return f"Course not found..."
        else:
            course['hours'] = hours
            return f"Course hours Updated!!!"
        
    def updatelessons(self, courseId: int, lessons: float)-> str:
        course = self._mycourses[courseId]
        if course is None:
            return f"Course not found..."
        else:
            course['lessons'] = lessons
            return f"Course lessons Updated!!!"
        
    def updateachievements(self, courseId: int, achievements: float)-> str:
        course = self._mycourses[courseId]
        if course is None:
            return f"Course not found..."
        else:
            course['achievements'] = achievements
            return f"Course Achievements Updated!!!"
        
    def updateCourse(self, courseId: int, progress: float, hours: float, lessons: int, achievements: int) -> str:
        self.updateprogress(courseId, progress)
        self.updatehours(courseId, hours)
        self.updatelessons(courseId, lessons)
        self.updateachievements(courseId, achievements)
        return f"Course {courseId} updated Successfully!!!"
    
    def __repr__(self)-> str:
        return f"class <Student>"
    
    def __str__(self) -> str:
        return f"SR Number: {self.sr_no}\nStudent Name: {self.fullname}\nEmail: {self.email}\nAnimation Type: {self.animation_Type}\nSoftware: {self.software}\nLearning Language: {self.lang}\nAuto-Earn: {self.auto_Earn}\nKisok: {self.kiosk}\nEducational Email: {self.edu_email}"
    
    def change_LMS_id(self, _new_id) -> str:
        self.LMS_id = _new_id
        return f"New LMS ID Linked to your Portal."

@final   
class Instructor(User):
    _sr_counter = count(start=1)
    def __init__(self, fullname: str, email: str, _passwrd: str, field: str):
        super().__init__(fullname, email, _passwrd)
        self.field = field
        self.sr_no: int = next(Instructor._sr_counter)

    def __repr__(self) -> str:
        return f"Class <User>"
    def __str__(self) -> str:
        return f"Sr No: {self.sr_no}\nFull Name: {self.fullname}\nEmail: {self.email}\nField: {self.field}"
    
class Ago(Instructor):
    pass

def main() -> None:
    s1 = Student(fullname="Muhammad Awais", email="mawais9028@gmail.com", _passwrd="123456", animation_Type="3D Animation", software="Maya", lang="Urdu", auto_Earn=False, kiosk=True, edu_email="bcs21201@pu.edu.pk")

    print("Student Details........................")
    print(s1)
    print("\nStudent's Joining Date...............\n")
    print(s1._get_joining_date)
    print("\nStudent trying changing password............\n")
    print(s1.change_passwrd("123456", "aassaa"))
    print("\nStudent Checking his All Courses......\n")
    print(s1.mycourses_summary)
    print("\nStudent Enrolling in the course 5................\n")

    print(s1.enroll_course(5))
    print("\nStudent Checking all courses.........\n")
    print(s1.mycourses_summary)
    print("\nUpdating Course 5...........\n")
    print(s1.updateCourse(courseId=5,progress=6.5,hours=3.5,lessons=5,achievements=7))
    print("\nChecking all courses........\n")
    print(s1.mycourses_summary)
    print("\nEnrolling course 7.......\n")

    print(s1.enroll_course(7))
    print("\nAll Courses......\n")
    print(s1.mycourses_summary)
    print("\nUpdating Course 7........\n")
    print(s1.updateCourse(courseId=7,progress=12.5,hours=9,lessons=2,achievements=1))
    print("\nChecking all courses........\n")
    print(s1.mycourses_summary)
    print("\nChecking only Course 5.......\n")
    print("Let's check course 5 Summary for Student 1")
    print(s1.mycourse_summary(5))
    print("\nInstructor Section................\n")
    i1 = Instructor(fullname="Haisem", email="Haiisem@metaviz.pro", _passwrd="123456", field="AI")
    print(i1)
    print("\n\n")
    print(i1._get_joining_date)
    print("\n\n")
    print(i1.change_passwrd("1112", "3333"))
    print("\n\n")


main()




    
