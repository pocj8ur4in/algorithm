restaurants = int(input().rstrip())
customers = list(map(int, input().rstrip().split(" ")))
leader, follwer = list(map(int, input().rstrip().split(" ")))
answer = 0

for restaurant in range(0, restaurants):
    customer = customers[restaurant]

    if customers[restaurant] <= leader:
        answer += 1
        continue
    else:
        answer += 1
        customers[restaurant] -= leader

        answer += customers[restaurant] // follwer
        customers[restaurant] = customers[restaurant] % follwer

        if customers[restaurant] > 0:
            answer += 1

print(answer)

# 맞았습니다!	330ms	107MB
