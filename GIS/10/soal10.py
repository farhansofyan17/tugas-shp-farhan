import shapefile

w=shapefile.Writer("soal10",shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("dag","satu")
w.record("dig","dua")
w.record("dug","tiga")
w.record("krak","empat")
w.record("krik","lima")
w.record("kruk","enam")
w.record("krek","tujuh")
w.record("krok","delapan")

w.poly([[[1,1], [2,4], [3,1]]])
w.poly([[[1,5], [1,7], [5,6]]])
w.poly([[[4,1], [3,5], [5,5]]])
w.poly([[[3,7], [7,8], [7,6]]])
w.poly([[[6,3], [6,5], [10,4]]])
w.poly([[[5,2], [10,3], [10,1]]])
w.poly([[[9,6], [13,8], [11,4]]])
w.poly([[[11,2], [13,6], [15,4]]])

w.close()