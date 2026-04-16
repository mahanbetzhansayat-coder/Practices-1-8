from connect import get_connection

def upsert_contact_py():
    username = input("Username: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (username, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Saved")

def search_contacts_py():
    pattern = input("Pattern: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def show_paginated_py():
    lim = int(input("Limit: "))
    offs = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (lim, offs))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_contact_py():
    value = input("Username or phone: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")

def bulk_insert_py():
    names = ["Ayan", "Aliya", "Nurdaulet"]
    phones = ["87011234567", "87771231212", "123"]

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()
    print("Bulk insert executed")

while True:
    print("\n1. Upsert contact")
    print("2. Search contacts")
    print("3. Show paginated")
    print("4. Delete contact")
    print("5. Bulk insert")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        upsert_contact_py()
    elif choice == "2":
        search_contacts_py()
    elif choice == "3":
        show_paginated_py()
    elif choice == "4":
        delete_contact_py()
    elif choice == "5":
        bulk_insert_py()
    elif choice == "0":
        break
    else:
        print("Invalid choice")