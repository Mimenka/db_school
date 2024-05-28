from database import conn


def get_group_list(groups):
    result = []

    for group in groups:
        result.append({'id': group[0], 'name': group[1]})
    
    return result


def get_students_list(students):
    result = []
    con = conn.cursor()

    for student in students:
        con.execute(f'SELECT * FROM t_group WHERE id={student[3]}')
        group = con.fetchone()

        result.append({
            'id': student[0], 
            'first_name': student[1],
            'last_name': student[2],
            'group_name': group[1],
        })

    return result


def get_teachers_list(teachers):
    result = []
    con = conn.cursor()

    for teacher in teachers:
        con.execute(f'SELECT * FROM t_position WHERE id={teacher[3]}')
        position = con.fetchone()

        result.append({
            'id': teacher[0],
            'first_name': teacher[1],
            'last_name': teacher[2],
            'position_name': position[1],
        })

    return result


def get_subjects_list(subjects):
    result = []

    for subject in subjects:
        result.append({'id': subject[0], 'name': subject[1]})
    
    return result


def get_teachers_groups_list(teachers_groups):
    result = []
    con = conn.cursor()

    for tech_gr in teachers_groups:
        con.execute(f'SELECT * FROM t_teacher WHERE id={tech_gr[1]}')
        teacher = con.fetchone()

        con.execute(f'SELECT * FROM t_group WHERE id={tech_gr[2]}')
        group = con.fetchone()

        con.execute(f'SELECT * FROM t_subject WHERE id={tech_gr[3]}')
        subject = con.fetchone()

        result.append({
            'teacher_fullname': f'{teacher[1]} {teacher[2]}',
            'group_name': group[1],
            'subject_name': subject[1],
        })

    return result