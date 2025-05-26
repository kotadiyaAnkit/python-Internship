frits={"apple", "banana","apple", "orange" ,"banana", "mango"}

# print(frits.union())
union=frits.union()
print(union)

print("------------------------------------------")

#Track Unique Visitors on a Website
# Use Case: Count how many distinct users visited.


 
unique_visitors = set()

visitor_data = [
    'abc', 'abc', 'chatgpt', 'w3class', 'w3class'
]

unique_visitors= unique_visitors.union(set(visitor_data))
for ip in visitor_data:
    unique_visitors.add(ip)

print(f'Unique Visitors: {len(unique_visitors)}')

