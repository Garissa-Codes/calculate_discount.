# Calculate Discount

## **Overview**

The Calculate Discount program calculates the final price of an item after applying a discount. It determines whether the discount percentage qualifies for application (20% or higher). If the condition is met, the program applies the discount to the original price and returns the discounted price; otherwise, it returns the original price.

This program is interactive and user-friendly, making it suitable for quick price calculations.

## **Features**

**Threshold**-Based Discount Application: Discounts below 20% are ignored, ensuring only significant discounts are applied.

**Error Handling:** The program gracefully handles invalid inputs, providing specific error messages.

**Precision:** Outputs are formatted to two decimal places for clear and accurate results.

## **Requirements**

Python 3.6 or higher

## **Usage**

## Clone this repository

git clone <repository_url>

**Navigate to the project directory:**

## cd calculate_discount

**Run the script:**

python calculate_discount.py

## **Example**

**Input:**

Enter the original price: 100

Enter the discount percentage: 25

**Output:**

The final price after applying the discount is: $75.00

**Another Input:**

Enter the original price: 100

Enter the discount percentage: 15

**Output:**

No discount applied. The original price is: $100.00

## Error Handling Example

Input:

Enter the original price: abc

Output:

Invalid input. Please ensure you enter numeric values for both price and discount percentage.

Code Breakdown

## **Functionality:**

The calculate_discount function applies a simple formula for discount calculation if the discount percentage is 20% or higher.

User inputs are validated to prevent crashes due to invalid data types.

**Modularity:**

Key calculations are encapsulated in functions, making the code reusable and maintainable.

## **Contributing**

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## **License**

This project is licensed under the MIT License.
