import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for
def main():

    conn = sqlite3.connect("celebrities.db")


    cursor = conn.cursor()

    sql = "update celebs set photo=replace(photo,'http://www.nphinity.com/pics/','https://s3.amazonaws.com/isat3402019/')"
    cursor.executemany(sql)

    conn.commit()

    conn.close()



main()
