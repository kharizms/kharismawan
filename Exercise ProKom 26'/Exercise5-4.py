alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points for shooting the alien.") #menampilkan output karena kondisi terpenuhi
else:
    print("You just earned 10 points.") #false, tidak menampilkan output karena kondisi terpenuhi, sehingga tidak masuk ke blok else

alien_color = "yellow"

if alien_color == "green":
    print("You just earned 5 points for shooting the alien.") #false, tidak menampilkan output karena kondisi tidak terpenuhi
else:
    print("You just earned 10 points.") #menampilkan output karena kondisi tidak terpenuhi, sehingga masuk ke blok else