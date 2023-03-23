from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)

# Setting

status = model.Status
othello = model.Othello

@app.route('/',methods=['GET','POST'])
def index():
    global rows # definition of global variable
    if request.method == 'GET':
        global other_color
        other_color = 1
        rows = status.rows
        global turn_cnt
        turn_cnt = 0
    if request.method == 'POST':
        place = request.form['place']
        if turn_cnt % 2 == 0:
            color = 1 # black
        if turn_cnt % 2 == 1:
            color = 2 # white
        row_num = int(place.split('-')[0]) # 1~8
        column_num = int(place.split('-')[1]) # 1~8
        rows, place_check = othello.othello(rows,color,row_num,column_num)
        if place_check:
            turn_cnt += 1
            if turn_cnt % 2 == 0:
                other_color = 1 # black
            if turn_cnt % 2 == 1:
                other_color = 2 # white    
    # turn int into str
    rows_str = [list(map(str, row)) for row in rows]
    return render_template('index.html',rows_str=rows_str,color=str(other_color))


if __name__ == '__main__':
    app.run(port=5000, threaded=True)