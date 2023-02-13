price_for_one_page = float(input())
price_for_one_cover = float(input())
percent_for_sell = int(input())
sum_for_design = float(input())
percent_for_team = float(input())

sum_for_print = price_for_one_page * 899 + price_for_one_cover * 2
discount = sum_for_print - sum_for_print * (percent_for_sell/100)
price_for_design = discount + sum_for_design
totall_sum = price_for_design - price_for_design * (percent_for_team/100)

print(f"Avtonom should pay {totall_sum:.2f} BGN.")