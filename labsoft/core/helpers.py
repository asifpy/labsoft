import datetime


def common_form_excludes(approval_fields=False):
    COMMON_EXCLUDES = [
        'is_prepared',
        'prepared_by',
        'prepared_on'
        ]

    if not approval_fields:
        return COMMON_EXCLUDES
    else:
        APPROVAL_FIELDS = [
            'is_reviewed',
            'reviewed_by',
            'reviewed_on',
            'is_approved',
            'approved_by',
            'approved_on'
            ]
        return COMMON_EXCLUDES + APPROVAL_FIELDS


def make_preparation(instance, user):
    instance.prepared_on = datetime.datetime.now()
    instance.prepared_by = user
    instance.is_prepared = True
    instance.save()


def make_review(instance, user):
    instance.is_reviewed = True
    instance.reviewed_on = datetime.datetime.now()
    instance.reviewed_by = user
    instance.save()


def make_approve(instance, user):
    instance.approved_on = datetime.datetime.now()
    instance.approved_by = user
    instance.is_approved = True
    instance.save()
