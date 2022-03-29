
from parse import parse
from eclass.service.models import Course
from bs4 import BeautifulSoup

class Parser:
    def course_list(self, page):
        page_ = BeautifulSoup(page)
        courses = []
        for course in page_.select_one('div.course_lists').select('div.course_box'):
            id_ = parse("http://eclass.inha.ac.kr/course/view.php?id={id}", course.select_one('a')['href'])['id'])
            tmp = parse(
                "{name}[{unknown}-{course}-{section}]",
                course.select_one('div.course-name div.course-title').select_one('h3').contents[0].string
            )
            courses.append(
                Course(
                    id=id_,
                    name=tmp['name'],
                    number=tmp['number'],
                    section=tmp['section'],
                )
            )
        
        return courses
    
    def parse_course(self, page):
        page_ = BeautifulSoup(page)
        weeks = page_.select_one('div.total_sections > div.course_box')
        parsed_weeks = {}
        for week in weeks.select('.section.main'):
            self.parse_week(week)
            
    
    def parse_week(self, week):
        week_number = parse("{n}Week [{fr} - {to}]", week['aria-label'])['n']
        parsed_weeks[week_number] = []
        for activity in week.select('div.content > .section > .activity'):
            pass
    
    def parse_activity(self, activity):
        title = activity.select_one('div.activityinstance span.instancename').contents[0].string.strip()
        id_ = parse("module-{}", activity['id'])[0]
        type_ = "unknown" # None 
        if 'ubfile' in activity['class']:
            type_ = 'ubfile'
        elif 'vod' in  activity['class']:
            type_ = 'vod'
        elif 'folder' in  activity['class']:
            type_ = 'folder '

        parsed_weeks[week_number].append({"id":id_, "type":type_, "title":title})
        #parsed_weeks[week_number].append({type_:{"id":module}})
        #print(activity_instance.text)
    