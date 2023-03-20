from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def applicant_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login/job-seekers/'):
    '''
    Decorator for views that checks that the logged in user is a job-seeker, redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_applicant,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def organization_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login/organizations/'):
    '''
    Decorator for views that checks that the logged in user is an organization, redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_organization,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator