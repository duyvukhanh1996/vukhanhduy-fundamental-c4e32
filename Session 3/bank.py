cash_at_bank = 21
interest_rate = 6.5 / 100
for i in range(9):
    cash_at_bank = cash_at_bank + cash_at_bank * interest_rate
print("sau 9 nam co :",cash_at_bank,"trieu")
cash_at_bank = 21
years = 0
while cash_at_bank < 1200:
    cash_at_bank = cash_at_bank + cash_at_bank * interest_rate
    years += 1
print("Sau",years,"nam thi mua duoc nha")