import java.util.Scanner;

public class LoginSystem {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        String correctUsername = "admin";
        String correctPassword = "secure123";

        int attempts = 3;

        while (attempts > 0) {

            System.out.print("Enter username: ");
            String username = input.nextLine();

            System.out.print("Enter password: ");
            String password = input.nextLine();

            if (username.equals(correctUsername) && password.equals(correctPassword)) {
                System.out.println("Login successful!");
                break;
            } else {
                attempts--;
                System.out.println("Incorrect login. Attempts left: " + attempts);
            }

        }

        if (attempts == 0) {
            System.out.println("Account locked.");
        }

        input.close();
    }
}
