# Permissions & Groups Setup

- Custom permissions are defined in `Book` model: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Groups:
  - Viewers → can_view
  - Editors → can_view, can_create, can_edit
  - Admins → all permissions
- Views are protected with @permission_required decorators.
- Users must be assigned to one of these groups to access features.
