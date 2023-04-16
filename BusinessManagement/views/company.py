from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
import traceback as tb

company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # rr284 April 9 2023
    # don't do SELECT *
    query = """SELECT id, name, address, city, country, state, zip, website,
            (SELECT count(*) from IS601_MP3_Employees A
            WHERE A.company_id = B.id) AS employees
            FROM IS601_MP3_Companies B
            WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # rr284 April 9 2023

    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = int(request.args.get("limit", "10"))

    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"
    
    if country:
        query += " AND country = %(country)s"
        args["country"] = country
    
    if state:
        query += " AND state = %(state)s"
        args["state"] = state
        
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
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
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        print(tb.format_exc())
        flash(f"Unexpected error while trying to search company data: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(col,col) for col in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

# rr284 April 9 2023
@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # rr284 April 9 2023

        data = {}
        has_error = False # use this to control whether or not an insert occurs
        
        data["name"] = request.form.get("name")
        data["address"] = request.form.get("address")
        data["city"] = request.form.get("city")
        data["state"] = request.form.get("state")
        data["country"] = request.form.get("country")
        data["zip_code"] = request.form.get("zip")
        data["website"] = request.form.get("website")

        for k,v in data.items():
            if k!="website" and not v:
                flash(f"{k} is a required field", "danger")
                has_error = True
            elif k=="website" and not v:
                data[k] = None
                
        # checking valid state and country
        if data["state"]:
            try:
                state = pycountry.subdivisions.get(code = data["state"])
            except KeyError:
                flash("Invalid state selected", "danger")
                has_error = True
        if data["country"]:
            try:
                country = pycountry.countries.get(name = data["country"])
            except KeyError:
                flash("Invalid country selected", "danger")
                has_error = True
        
        if not has_error:
            try:
                result = DB.insertOne(""" 
                INSERT INTO IS601_MP3_Companies (name, address, city, state, country, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, *data.values()) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                # rr284 April 9 2023
                print(tb.format_exc())
                flash(f"Unexpected error while trying to add company details: {e}", "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # rr284 April 9 2023

    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Company ID is missing - required", "danger")
        row = None
    else:
        if request.method == "POST":
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            # rr284 April 9 2023

            has_error = False # use this to control whether or not an insert occurs
            data = {}     
            data["name"] = request.form.get("name")
            data["address"] = request.form.get("address")
            data["city"] = request.form.get("city")
            data["country"] = request.form.get("country")
            data["state"] = request.form.get("state")
            data["zip_code"] = request.form.get("zip")
            data["website"] = request.form.get("website")
            data["id"] = id
            
            for k,v in data.items():
                if k!="website" and not v:
                    flash(f"{k} is a required field", "danger")
                    has_error = True
                elif k=="website" and not v:
                    data[k] = None
            
            # checking valid state and country
            if data["state"]:
                try:
                    state = pycountry.subdivisions.get(code = data["state"])
                except KeyError:
                    flash("Invalid state selected", "danger")
                    has_error = True
            if data["country"]:
                try:
                    country = pycountry.countries.get(name = data["country"])
                except KeyError:
                    flash("Invalid country selected", "danger")
                    has_error = True           
            
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies 
                    SET name = %s, address = %s, city = %s, country = %s, state = %s, zip = %s, website = %s
                    WHERE id = %s
                    """, *data.values())
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(tb.format_exc())
                    flash(f"Unexpected error while trying to edit company details", "danger")
        row = None
        try:
            # TODO edit-11 fetch the updated data
            # rr284 April 9 2023
            result = DB.selectOne("SELECT * FROM IS601_MP3_Companies WHERE id = %s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-12 make this user-friendly
            print(tb.format_exc())
            flash(f"Unexpected error while trying to fetch the updated company details", "danger")
    # TODO edit-13 pass the company data to the render template
    country = None
    state = None
    if row:
        country = row.get("country")
        state = row.get("state")
    return render_template("edit_company.html", row=row, country = country, state = state)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    # rr284 April 9 2023
    if request.method == "GET":
        id = request.args.get("id")
        if not id:
            flash("Company ID is missing - required", "danger")
            return render_template("list_companies.html", **request.args)
        try:
            constraint_fix = DB.update("""
            UPDATE IS601_MP3_Employees
            SET company_id = NULL
            WHERE company_id = %s
            """, id)

            result = DB.delete("""
            DELETE FROM IS601_MP3_Companies
            WHERE id = %s
            """, id)

            if constraint_fix.status and result.status:
                flash("Successfully deleted company", "success")
        except Exception as e:
            flash(f"Unexpected error while trying to delete the Company: {e}", "danger")
            return render_template("list_companies.html", **request.args)
        new_args = dict(request.args)
        del new_args["id"]
    return redirect(url_for('company.search', **new_args))

