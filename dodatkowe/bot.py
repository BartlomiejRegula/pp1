def bot():
    import turtle

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Move the turtle to the starting position
    t.setpos(0, -100)
    t.pendown()

    # Draw the semicircle
    t.circle(100, extent=180)

    # Hide the turtle and hold the window open
    t.ht()
    turtle.mainloop()
print(bot())