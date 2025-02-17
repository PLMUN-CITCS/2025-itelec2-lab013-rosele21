# 2025-ITELEC2-LAB013
Week 05 - Looping Statements

Laboratory # 13 - Guided Coding Exercise: for Loop with break and continue

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 13 - Guided Coding Exercise: for Loop with break and continue**

   **Objective:**
   - Understand what a loop is and its advantages (automating repetitive tasks).
   - Learn how to iterate over a sequence using a for loop.
   - Use the break statement to exit a loop early.
   - Use the continue statement to skip certain iterations.

   **Desired Output:**
   ```bash
   1
   2
   4
   5
   6
   ```

   **Notable Observations (to be discussed after completing the exercise):**
   - The continue statement skips only the current iteration of the loop. The loop continues with the next item.
   - The break statement terminates the entire loop. No further iterations are performed.
   - The placement of the if statements and the print() statement within the loop is crucial to achieving the desired behavior.

   **Python Best Practices**
   - Descriptive Variable Names: Use meaningful variable names (e.g., numbers instead of nums, num instead of n).
   - Inline Comments: Use comments to clarify the purpose of break and continue, especially in more complex loops.
   - Proper Indentation: Consistent indentation is essential for Python code to work correctly. Make sure the code inside the loop and the if statements is properly indented.
   - Loop Logic: Carefully consider the logic of your loop, including where you place your if statements, continue, break, and print statements to ensure the loop behaves as intended.
   - Test Thoroughly: Test your code with different ranges and conditions to ensure it works correctly in various scenarios.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `for_loop_break_continue.py`
      
   2.  Define a list of numbers from 1 to 10:
      - Use the range() function and the list() constructor to create a list of numbers from 1 to 10 (inclusive). Store it in a variable named numbers.
```python
numbers = list(range(1, 11))
```
      
   3.  Iterate over each number using a for loop:
      - Use a for loop to iterate through each num in the numbers list.
```python
for num in numbers:
```

   4. Skip the number 3 using continue:
      - Inside the for loop, use an if statement to check if num is equal to 3.
      - If it is, use the continue statement. This will immediately skip the rest of the current iteration of the loop and jump to the next number.
```python
    if num == 3:
        continue  # Skip the rest of this iteration
```

   5. If the number is 7, exit the loop using break:
      - After the if statement that checks for 3, use another if statement to check if num is equal to 7.
      - If it is, use the break statement. This will terminate the entire for loop.
```python
    if num == 7:
        break  # Exit the loop completely
```

   6. Print the current number:
      - After the if statements, use the print() function to display the current value of num. This print() statement will only be executed if neither the continue nor the break conditions are met.
```python
    print(num)
```

   7. Complete Code: Combine the steps above to form the complete program.
   8. Run the code: Execute your Python code.
   9. Observe the output: Verify that the output matches the "Desired Output" shown above.

   **Conclusion**
   This exercise introduced the for loop, a powerful tool for automating repetitive tasks.  You learned how to use the continue statement to skip specific iterations and the break statement to exit a loop early.  These control flow mechanisms provide flexibility and control over loop execution, allowing you to create more sophisticated and efficient programs.  Understanding how break and continue modify loop behavior is crucial for writing effective Python code.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 13"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
