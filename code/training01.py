# ポリモーフィズムなし
shapelist = [triangletype, circletype]
for shape in shapelist:
# このループによってデータ型の確認を行っている
    if isinstance(shape, Triangle):
        shape.drew_triangle()
    if isinstance(shape.Circle):
        shape.draw_circle()

#ポリモーフィズムを実装
shapelist = [triangletype, circletype]
for shape in shapelist:
    shape.draw()