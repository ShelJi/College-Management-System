from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}"
    

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    SYLLABUS_COVERAGE_CHOICES = [
        ("below_30", "Below 30%"),
        ("30_54", "30 to 54%"),
        ("55_69", "55 to 69%"),
        ("70_84", "70 to 84%"),
        ("85_100", "85 to 100%"),
    ]
    syllabus_coverage = models.CharField(max_length=50, choices=SYLLABUS_COVERAGE_CHOICES)

    TEACHER_PREP_CHOICES = [
        ("not_at_all", "Won’t teach at all"),
        ("indifferent", "Indifferently"),
        ("poor", "Poorly"),
        ("satisfactory", "Satisfactorily"),
        ("thorough", "Thoroughly"),
    ]
    teacher_preparation = models.CharField(max_length=50, choices=TEACHER_PREP_CHOICES)

    COMMUNICATION_CHOICES = [
        ("very_poor", "Very poor communication"),
        ("ineffective", "Generally ineffective"),
        ("satisfactory", "Just satisfactorily"),
        ("sometimes_effective", "Sometimes effective"),
        ("always_effective", "Always effective"),
    ]
    teacher_communication = models.CharField(max_length=50, choices=COMMUNICATION_CHOICES)

    TEACHING_APPROACH_CHOICES = [
        ("poor", "Poor"),
        ("fair", "Fair"),
        ("good", "Good"),
        ("very_good", "Very good"),
        ("excellent", "Excellent"),
    ]
    teaching_approach = models.CharField(max_length=50, choices=TEACHING_APPROACH_CHOICES)

    EVALUATION_FAIRNESS_CHOICES = [
        ("unfair", "Unfair"),
        ("usually_unfair", "Usually unfair"),
        ("sometimes_unfair", "Sometimes unfair"),
        ("usually_fair", "Usually fair"),
        ("always_fair", "Always fair"),
    ]
    evaluation_fairness = models.CharField(max_length=50, choices=EVALUATION_FAIRNESS_CHOICES)

    ASSIGNMENT_DISCUSSION_CHOICES = [
        ("never", "Never"),
        ("rarely", "Rarely"),
        ("sometimes", "Occasionally/Sometimes"),
        ("usually", "Usually"),
        ("every_time", "Every time"),
    ]
    assignment_discussion = models.CharField(max_length=50, choices=ASSIGNMENT_DISCUSSION_CHOICES)

    INTERNSHIP_OPPORTUNITY_CHOICES = [
        ("never", "Never"),
        ("rarely", "Rarely"),
        ("sometimes", "Sometimes"),
        ("often", "Often"),
        ("regularly", "Regularly"),
    ]
    internship_opportunities = models.CharField(max_length=50, choices=INTERNSHIP_OPPORTUNITY_CHOICES)

    MENTORING_EFFECTIVENESS_CHOICES = [
        ("not_at_all", "Not at all"),
        ("marginally", "Marginally"),
        ("moderately", "Moderately"),
        ("very_well", "Very well"),
        ("significantly", "Significantly"),
    ]
    mentoring_effectiveness = models.CharField(max_length=50, choices=MENTORING_EFFECTIVENESS_CHOICES)

    LEARNING_OPPORTUNITIES_CHOICES = [
        ("strongly_disagree", "Strongly disagree"),
        ("disagree", "Disagree"),
        ("neutral", "Neutral"),
        ("agree", "Agree"),
        ("strongly_agree", "Strongly agree"),
    ]
    learning_opportunities = models.CharField(max_length=50, choices=LEARNING_OPPORTUNITIES_CHOICES)

    COMPETENCY_INFO_CHOICES = ASSIGNMENT_DISCUSSION_CHOICES
    competency_info = models.CharField(max_length=50, choices=COMPETENCY_INFO_CHOICES)

    MENTOR_FOLLOWUP_CHOICES = [
        ("no_mentor", "I don’t have a mentor"),
        ("rarely", "Rarely"),
        ("sometimes", "Occasionally/Sometimes"),
        ("usually", "Usually"),
        ("every_time", "Every time"),
    ]
    mentor_followup = models.CharField(max_length=50, choices=MENTOR_FOLLOWUP_CHOICES)

    TEACHING_EXAMPLES_CHOICES = COMPETENCY_INFO_CHOICES
    teaching_examples = models.CharField(max_length=50, choices=TEACHING_EXAMPLES_CHOICES)

    STRENGTH_IDENTIFICATION_CHOICES = [
        ("unable", "Unable to"),
        ("slightly", "Slightly"),
        ("partially", "Partially"),
        ("reasonably", "Reasonably"),
        ("fully", "Fully"),
    ]
    strength_identification = models.CharField(max_length=50, choices=STRENGTH_IDENTIFICATION_CHOICES)

    WEAKNESS_HELP_CHOICES = COMPETENCY_INFO_CHOICES
    weakness_help = models.CharField(max_length=50, choices=WEAKNESS_HELP_CHOICES)

    STUDENT_ENGAGEMENT_CHOICES = LEARNING_OPPORTUNITIES_CHOICES
    student_engagement = models.CharField(max_length=50, choices=STUDENT_ENGAGEMENT_CHOICES)

    STUDENT_CENTRIC_METHODS_CHOICES = [
        ("not_at_all", "Not at all"),
        ("very_little", "Very little"),
        ("somewhat", "Somewhat"),
        ("moderate", "Moderate"),
        ("great_extent", "To a great extent"),
    ]
    student_centric_methods = models.CharField(max_length=50, choices=STUDENT_CENTRIC_METHODS_CHOICES)

    EXTRACURRICULAR_CHOICES = LEARNING_OPPORTUNITIES_CHOICES
    extracurricular = models.CharField(max_length=50, choices=EXTRACURRICULAR_CHOICES)

    SOFT_SKILLS_CHOICES = STUDENT_CENTRIC_METHODS_CHOICES
    soft_skills = models.CharField(max_length=50, choices=SOFT_SKILLS_CHOICES)
    
    principal_quality = models.CharField(max_length=50, choices=STUDENT_CENTRIC_METHODS_CHOICES, null=True, blank=True)

    ICT_USAGE_CHOICES = [
        ("below_29", "Below 29%"),
        ("30_49", "30 – 49%"),
        ("50_69", "50 – 69%"),
        ("70_89", "70 – 89%"),
        ("above_90", "Above 90%"),
    ]
    ict_usage = models.CharField(max_length=50, choices=ICT_USAGE_CHOICES)
    """
    ICT Usage refers to how much Information and Communication Technology (ICT) tools (like LCD projectors, 
    multimedia presentations, smartboards, and online learning platforms) are used in teaching.
    """

    OVERALL_QUALITY_CHOICES = LEARNING_OPPORTUNITIES_CHOICES
    overall_quality = models.CharField(max_length=50, choices=OVERALL_QUALITY_CHOICES)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey by {self.user.username} on {self.submitted_at}"
