import traceback as tb
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re

employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # rr284 April 9 2023

    query = """SELECT A.id, first_name, last_name, email, company_id, IF(name is not null, name, 'N/A') as company_name
    FROM IS601_MP3_Employees A LEFT JOIN IS601_MP3_Companies B on A.company_id = B.id
    WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # TODO search-3 append like filter for first_name if provided
    # TODO search-4 append like filter for last_name if provided
    # TODO search-5 append like filter for email if provided
    # TODO search-6 append equality filter for company_id if provided
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    # rr284 April 9 2023

    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = int(request.args.get("limit", '10'))

    if fn:
        query += " AND first_name LIKE %(fn)s"
        args["fn"] = f"%{fn}%"  
    if ln:
        query += " AND last_name LIKE %(ln)s"
        args["ln"] = f"%{ln}%"
    if email:
        query += " AND email LIKE %(email)s"
        args["email"] = f"%{email}%"
    if company:
        query += " AND company_id = %(company)s"
        args["company"] = company
    if column and order: 
        if column in allowed_columns and order in ['asc', 'desc']:
            query += f" ORDER BY {column} {order}"
    try:
        if limit < 1 or limit > 100:
            raise ValueError("Limit should be between 1 and 100")
    except ValueError:
        flash("Limit should be between 1 and 100, defaulting to 10", "danger")
        limit = 10
    query += " LIMIT %(limit)s"
    args["limit"] = limit

    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        
        # TODO search-10 make message user friendly
        # rr284 April 9 2023

        flash(f"Unexpected error while searching employee data: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(col,col) for col in allowed_columns]
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        # rr284 April 9 2023

        has_error = False # use this to control whether or not an insert occurs
        data = {}
        data["first_name"] = request.form.get("first_name")
        data["last_name"] = request.form.get("last_name")
        data["company"] = request.form.get("company") or None
        data["email"] = request.form.get("email")
        # for checking invalid email format
        pattern = "[^@]+@[^@]+\.[^@]+"
        if not re.match(pattern, data["email"]):
            flash("Invalid email format", "danger")
            has_error = True
        
        for key, val in data.items():
            if key!="company" and not val:
                flash(f"{key} is a required field", "danger")
                has_error = True
                
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees(first_name, last_name, company_id, email)
                VALUES (%s, %s, %s, %s)
                """, *data.values()
                ) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                # rr284 April 9 2023

                print(tb.format_exc())
                flash(f"Unexpected error while adding employee details: {e}", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # rr284 April 9 2023

    id = request.args.get('id')
    if not id: # TODO update this for TODO edit-1
        flash("Employee ID is required", "danger")
        row = None
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            has_error = False # use this to control whether or not an insert occurs

            data = {}
            data["first_name"] = request.form.get("first_name")
            data["last_name"] = request.form.get("last_name")
            data["company"] = request.form.get("company") or None
            data["email"] = request.form.get("email")
            data["id"] = id
            # for checking invalid email format
            pattern = "[^@]+@[^@]+\.[^@]+"
            if not re.match(pattern, data["email"]):
                flash("Invalid email format", "danger")
                has_error = True
        
            for key, val in data.items():
                if key!="company" and not val:
                    flash(f"{key} is a required field", "danger")
                    has_error = True
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees
                    SET first_name = %s, last_name = %s, company_id = %s, email = %s
                    WHERE id = %s
                    """, *data.values())
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    print(tb.format_exc())
                    flash(f"Unexpected error while trying to edit employee details: {e}", "danger")
        row = None
        try:
            # TODO edit-8 fetch the updated data 
            # rr284 April 9 2023
            result = DB.selectOne("""
            SELECT * FROM IS601_MP3_Employees A
            LEFT JOIN IS601_MP3_Companies B on A.company_id = B.id
            WHERE A.id = %s
            """, id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            print(tb.format_exc())
            flash(f"Unexpected error while fetching the updated employee details: {e}", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row, company=row.get("company_id"))

@employee.route("/delete", methods=["GET"])
def delete():
    
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    # rr284 April 9 2023
    
    if request.method == "GET":
        id = request.args.get("id")
        if not id:
            flash("Missing Employee ID", "danger")
            return render_template("list_employees.html")
        try:
            result = DB.delete("""
            DELETE FROM IS601_MP3_Employees
            WHERE id = %s
            """, id)
            if result.status:
                flash(f"Successfully deleted Employee", "success")
        except Exception as e:
            flash(f"Unexpected error while deleting the employee: {e}", "danger")
        new_args = dict(request.args)
        del new_args["id"]
    return redirect(url_for("employee.search", **new_args))
