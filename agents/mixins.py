from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect



class OrganaisorAndLoginRequiredMixin(AccessMixin):
    # Verify that the current user is authenticated and is an organaisor! 
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organaisor:
            return redirect('leads:lead-list')
        return super().dispatch(request, *args, **kwargs)