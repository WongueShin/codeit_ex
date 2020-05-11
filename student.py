class Student:
    # 코드를 쓰세요
    def __init__(self, name, idnum, major):
        self.info_manage = InfoManage(name, major, idnum)
        self.student_info = Info(self.info_manage.gpa, self.info_manage.name, self.info_manage.major,
                                 self.info_manage.idnum)
        self.average_gpa = AverageGpa(self.student_info.out_val())
        self.printer = Printer(self.student_info.out_val(), self.average_gpa.average(self.student_info.out_val()))


class Printer:
    def __init__(self, vallist, average_val):
        self.name = vallist[0]
        self.gpa = average_val
        self.major = vallist[2]
        self.idnum = vallist[3]

    def renewval (self, vallist, average_val):
        self.name = vallist[0]
        self.gpa = average_val
        self.major = vallist[2]
        self.idnum = vallist[3]

    def print_report_card(self, vallist, average_val):
        self.renewval(vallist, average_val)
        print(f'코드잇 대학 성적표\n\n학생 이름:{self.name}\n학생 번호:{self.idnum}\n소속 학과:{self.major}\n평균 학점:{average_val}')


class AverageGpa:
    def __init__(self, vallist):
        self.average_val = 'test'
        self.placeholder = 0
        self.length = 1
        self.i = 0
        self.gpa_val = vallist[1]

    def renewval(self, vallist):
        self.gpa_val = vallist[1]

    def average(self, vallist):
        self.renewval(vallist)
        #print('AverageGpa.gpa_val'+str(self.gpa_val))
        self.placeholder = 0
        for self.i in self.gpa_val:
            self.placeholder += self.i
        #print('AverageGpa.placeholder= '+str(self.placeholder))
        self.length = len(self.gpa_val)
        #print('AverageGpa.length= ' + str(self.length))
        if len(self.gpa_val) <= 0:
            self.length = 1
            #print('test if')
        self.average_val = self.placeholder / self.length
        #print('AverageGpa.average_val= '+str(self.average_val))
        return self.average_val


class Info:
    def __init__(self, gpa, name, major, idnum):
        self.gpa = gpa
        self.name = name
        self.major = major
        self.idnum = idnum
        self.vallist = [self.name, self.gpa, self.major, self.idnum]

    def input_renew_val (self, vallist):
        self.name = vallist[0]
        self.gpa = vallist[1]
        self.major = vallist[2]
        self.idnum = vallist[3]
        self.vallist = [self.name, self.gpa, self.major, self.idnum]

    def out_val(self):
        return self.vallist


class InfoManage:
    def __init__(self, name, major, idnum):
        self._gpa = []
        self._name = name
        self._major = major
        self._idnum = idnum

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, new_val):
        self._gpa = new_val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        self._name = new_val

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, new_val):
        self._major = new_val

    @property
    def idnum(self):
        return self._idnum

    @idnum.setter
    def idnum(self, new_val):
        self._idnum = new_val

    def change_student_info(self, name, idnum, major):
        self.name = name
        self.idnum = idnum
        self.major = major

    def add_grade(self, val):
        self.gpa.append(val)

    def renew_row_val(self):
        vallist = [self.name, self.gpa, self.major, self.idnum]
        return vallist



# 작성한 클래스에 맞춰서 실행 코드도 바꿔보세요
# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.info_manage.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.info_manage.add_grade(3.0)
younghoon.info_manage.add_grade(3.33)
younghoon.info_manage.add_grade(3.67)
younghoon.info_manage.add_grade(4.3)
younghoon.student_info.input_renew_val(younghoon.info_manage.renew_row_val())
#print('test'+str(younghoon.student_info.gpa))
#print('average'+str(younghoon.average_gpa.gpa_val))
# 학생 성적표
younghoon.printer.print_report_card(younghoon.student_info.out_val(), younghoon.average_gpa.average(younghoon.student_info.out_val()))
