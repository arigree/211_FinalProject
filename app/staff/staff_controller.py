# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_controller.py
# Description: Define the staff controller class

from flask import render_template, request, redirect, url_for
from .staff_manager import StaffManager


class StaffController:
    #  Displays all staff members
    @staticmethod
    def index():
        message = request.args.get('message', None)

        result = StaffManager.get_staff()

        if isinstance(result, str):
            return render_template(
                'staffs.html',
                staff_members=[],
                error_message=result,
                status_message=None,
                query=None
            )
        else:
            return render_template(
                'staffs.html',
                staff_members=result,
                error_message=None,
                status_message=message,
                query=None
            )

    #  Displays a single staff member's details
    @staticmethod
    def detail(staff_id):
        message = request.args.get('message', None)

        result = StaffManager.get_staff_member(staff_id)

        if isinstance(result, str):
            return render_template(
                'staffs.html',
                staff_members=[],
                error_message=result,
                status_message=None,
                query=None
            )
        else:
            return render_template(
                'detail.html',
                staff=result,
                status_message=message,
                error_message=None
            )

    @staticmethod
    def rentals(staff_id):
        result = StaffManager.get_staff_rentals(staff_id)

        if isinstance(result, str):
            return render_template(
                'staffs.html',
                staff_members=[],
                error_message=result,
                status_message=None,
                query=None
            )

        staff_member, rentals = result
        return render_template(
            'staff_rentals.html',
            staff=staff_member,
            rentals=rentals,
            error_message=None
        )

    #  Searches for staff members by name
    @staticmethod
    def search():
        search_query = request.args.get('query', None)
        result = StaffManager.search_staff(search_query)

        if isinstance(result, str):
            return render_template(
                'staffs.html',
                staff_members=[],
                error_message=result,
                status_message=None,
                query=search_query
            )
        else:
            return render_template(
                'staffs.html',
                staff_members=result,
                error_message=None,
                status_message=None,
                query=search_query
            )

    #  Creates a new staff member
    @staticmethod
    def create():
        if request.method == 'POST':
            staff_data = {
                'first_name': request.form.get('first_name', ''),
                'last_name': request.form.get('last_name', ''),
                'username': request.form.get('username', ''),
                'email': request.form.get('email', ''),
                'role': request.form.get('role', ''),
                'phone': request.form.get('phone', ''),
                'address': request.form.get('address', '')
            }

            result = StaffManager.create_staff(staff_data)

            if isinstance(result, str):
                return render_template(
                    'staff_form.html',
                    page_title='Create Staff',
                    submit_label='Create Staff',
                    form_action=url_for('staff.create'),
                    staff_data=staff_data,
                    error_message=result
                )
            else:
                return redirect(
                    url_for(
                        'staff.index',
                        message='Staff member successfully created'
                    )
                )

        return render_template(
            'staff_form.html',
            page_title='Create Staff',
            submit_label='Create Staff',
            form_action=url_for('staff.create'),
            staff_data={
                'first_name': '',
                'last_name': '',
                'username': '',
                'email': '',
                'role': '',
                'phone': '',
                'address': ''
            },
            error_message=None
        )

    #  Displays the staff member creation form
    @staticmethod
    def edit(staff_id):
        if request.method == 'GET':
            staff_member = StaffManager.get_staff_member(staff_id)

            if isinstance(staff_member, str):
                return render_template(
                    'staffs.html',
                    staff_members=[],
                    error_message=staff_member,
                    status_message=None,
                    query=None
                )

            return render_template(
                'staff_form.html',
                page_title='Edit Staff',
                submit_label='Save Changes',
                form_action=url_for('staff.edit', staff_id=staff_id),
                staff_data={
                    'first_name': staff_member.first_name,
                    'last_name': staff_member.last_name,
                    'username': staff_member.username,
                    'email': staff_member.email,
                    'role': staff_member.role,
                    'phone': staff_member.phone,
                    'address': staff_member.address
                },
                error_message=None
            )

        form_data = request.form.to_dict()
        result = StaffManager.update_staff(staff_id, form_data)

        if isinstance(result, str):
            return render_template(
                'staff_form.html',
                page_title='Edit Staff',
                submit_label='Save Changes',
                form_action=url_for('staff.edit', staff_id=staff_id),
                staff_data=form_data,
                error_message=result
            )

        return redirect(
            url_for(
                'staff.index',
                message='Staff member successfully updated'
            )
        )

    #  Deletes a staff member
    @staticmethod
    def delete(staff_id):
        if request.method == 'GET':
            staff_member = StaffManager.get_staff_member(staff_id)

            if isinstance(staff_member, str):
                return render_template(
                    'staffs.html',
                    staff_members=[],
                    error_message=staff_member,
                    status_message=None,
                    query=None
                )

            return render_template(
                'staff_delete.html',
                staff=staff_member,
                error_message=None
            )

        result = StaffManager.delete_staff(staff_id)

        if isinstance(result, str):
            staff_member = StaffManager.get_staff_member(staff_id)

            if isinstance(staff_member, str):
                return render_template(
                    'staffs.html',
                    staff_members=[],
                    error_message=result,
                    status_message=None,
                    query=None
                )

            return render_template(
                'staff_delete.html',
                staff=staff_member,
                error_message=result
            )

        return redirect(
            url_for(
                'staff.index',
                message='Staff member successfully deleted'
            )
        )