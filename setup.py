"""
Setup script for the Open edX package.
"""

from setuptools import setup

setup(
    name="Open edX",
    version="0.4",
    install_requires=["distribute"],
    requires=[],
    # NOTE: These are not the names we should be installing.  This tree should
    # be reorganized to be a more conventional Python tree.
    packages=[
        "openedx.core.djangoapps.course_groups",
        "openedx.core.djangoapps.user_api",
        "openedx.core.djangoapps.grading_policy",
        "lms",
        "cms",
    ],
    # pylint: disable=line-too-long
    entry_points={
        "openedx.course_tab": [
            "ccx = lms.djangoapps.ccx.plugins:CcxCourseTab",
            "courseware = lms.djangoapps.courseware.tabs:CoursewareTab",
            "course_info = lms.djangoapps.courseware.tabs:CourseInfoTab",
            "discussion = lms.djangoapps.django_comment_client.forum.views:DiscussionTab",
            "edxnotes = lms.djangoapps.edxnotes.plugins:EdxNotesTab",
            "external_discussion = lms.djangoapps.courseware.tabs:ExternalDiscussionCourseTab",
            "external_link = lms.djangoapps.courseware.tabs:ExternalLinkCourseTab",
            "html_textbooks = lms.djangoapps.courseware.tabs:HtmlTextbookTabs",
            "instructor = lms.djangoapps.instructor.views.instructor_dashboard:InstructorDashboardTab",
            "notes = lms.djangoapps.notes.views:NotesTab",
            "pdf_textbooks = lms.djangoapps.courseware.tabs:PDFTextbookTabs",
            "progress = lms.djangoapps.courseware.tabs:ProgressTab",
            "static_tab = xmodule.tabs:StaticTab",
            "syllabus = lms.djangoapps.courseware.tabs:SyllabusTab",
            "teams = lms.djangoapps.teams.plugins:TeamsTab",
            "textbooks = lms.djangoapps.courseware.tabs:TextbookTabs",
            "wiki = lms.djangoapps.course_wiki.tab:WikiTab",

            # ORA 1 tabs (deprecated)
            "peer_grading = lms.djangoapps.open_ended_grading.views:PeerGradingTab",
            "staff_grading = lms.djangoapps.open_ended_grading.views:StaffGradingTab",
            "open_ended = lms.djangoapps.open_ended_grading.views:OpenEndedGradingTab",
        ],
        "openedx.user_partition_scheme": [
            "random = openedx.core.djangoapps.user_api.partition_schemes:RandomUserPartitionScheme",
            "cohort = openedx.core.djangoapps.course_groups.partition_scheme:CohortPartitionScheme",
        ],
        "openedx.grading_policy": [
            "vertical = openedx.core.djangoapps.grading_policy.vertical:VerticalGrading",
            "sequential = openedx.core.djangoapps.grading_policy.sequential:SequentialGrading",
        ],
        "openedx.graders": [
            "WeightedSubsectionsGrader = openedx.core.djangoapps.grading_policy.graders.weighted_subs:WeightedSubsectionsGrader",
            "SingleSectionGrader = openedx.core.djangoapps.grading_policy.graders.single_section:SingleSectionGrader",
            "AssignmentFormatGrader = openedx.core.djangoapps.grading_policy.graders.assignment_format:AssignmentFormatGrader",
            "WeightedAssignmentFormatGrader = openedx.core.djangoapps.grading_policy.graders.weighted_assignment_format:WeightedAssignmentFormatGrader",
        ]
    }
)
