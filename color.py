import matplotlib.pyplot as plt
BP=[100,120,140,160,180,200,220]
Days=['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
size=[100,120,140,160,180,200,220]
color=[50,100,150,200,250,300,350]

plt.scatter(
            Days,
            BP,
            s=size,
            marker='o',
            c=color,
            cmap='viridis'
             
            )

plt.xlabel('Days')
plt.ylabel('Increase BP')
plt.title('Pressure Blood')
plt.show()

# Second graph
plt.scatter(
            Days,
            BP,
            s=size,
            marker='o',
            c='red',
            cmap='viridis'
             
            )

plt.xlabel('Days')
plt.ylabel('Increase BP')
plt.title('Pressure Blood')
plt.show()
