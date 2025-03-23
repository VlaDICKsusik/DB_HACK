import random
from datetime import date
from datacenter.models import Schoolkid, Chastisement, Mark, Subject, Commendation, Teacher


def get_student(full_name):
    return Schoolkid.objects.get(full_name__contains=full_name)


def get_subject(title, year_of_study):
    return Subject.objects.get(title=title, year_of_study=year_of_study)


def get_teacher(full_name):
    return Teacher.objects.get(full_name__contains=full_name)


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()

def create_commendation(schoolkid, subject, teacher):
    commendation_texts = [
        "Молодец!", "Отлично!", "Хорошо!", "Ты меня приятно удивил!",
        "Так держать!", "Замечательно!", "Здорово!", "Ты растешь над собой!",
        "Я тобой горжусь!", "Мы с тобой не зря поработали!"
    ]
    text = random.choice(commendation_texts)

    Commendation.objects.create(
        schoolkid=schoolkid,
        subject=subject,
        teacher=teacher,
        text=text,
        created=date.today()
    )


def main():

    student_name = "Фролов Иван"
    subject_name = "Музыка"
    teacher_name = "Селезнева Майя Макаровна"
    year_of_study = 6

    schoolkid = get_student(student_name)
    subject = get_subject(subject_name, year_of_study)
    teacher = get_teacher(teacher_name)

    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, subject, teacher)

    try:
        child = Schoolkid.objects.get(full_name__contains=student_name)
    except Schoolkid.DoesNotExist as child:
        print("не найден ученик с именем: ",child)
    else:
        print("Ученик найден")
    return child


if __name__ == "__main__":
    main()