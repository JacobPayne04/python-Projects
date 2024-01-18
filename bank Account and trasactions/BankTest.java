public class BankTest {
    public static void main(String[] args) {
        // Create 3 bank accounts

        BankAccount account1 = new BankAccount(900.00, 30.50);
        BankAccount account2 = new BankAccount(900.00, 30.50);
        BankAccount account3 = new BankAccount(900.00, 30.50);


        account1.displayStatus();
        System.out.println("*******************");
        account2.displayStatus();
        System.out.println("*******************");
        account3.displayStatus();
        System.out.println("*******************");



        System.out.println(BankAccount.getTotalMoney());


        // Deposit Test
        account1.setCheckingBalance(account1.getCheckingBalance()+200);
        account1.setSavingsBalance(account1.getSavingsBalance()+20);
        account1.displayStatus();
        System.out.println("*******************");

         account2.setCheckingBalance(account2.getCheckingBalance()+200);
        account2.setSavingsBalance(account2.getSavingsBalance()+20);
        account2.displayStatus();
        System.out.println("*******************");

         account3.setCheckingBalance(account3.getCheckingBalance()+200);
        account3.setSavingsBalance(account3.getSavingsBalance()+20);
        account3.displayStatus();
        System.out.println("*******************");




        // Withdrawal Test
        account1.setCheckingBalance(account1.getCheckingBalance()-200);
        account1.setSavingsBalance(account1.getSavingsBalance()-20);
        account1.displayStatus();
        System.out.println("*******************");

        account2.setCheckingBalance(account2.getCheckingBalance()-200);
        account2.setSavingsBalance(account2.getSavingsBalance()-20);
        account2.displayStatus();
        System.out.println("*******************");

        account3.setCheckingBalance(account3.getCheckingBalance()-200);
        account3.setSavingsBalance(account3.getSavingsBalance()-20);
        account3.displayStatus();
        System.out.println("*******************");

    

        
        // - deposit some money into each bank account's checking or savings account and
        // display the balance each time
        // - each deposit should increase the amount of totalMoney
        System.out.println(BankAccount.getTotalMoney());

      
        // - each withdrawal should decrease the amount of totalMoney

        // Static Test (print the number of bank accounts and the totalMoney)

        System.out.println(BankAccount.getAccounts());
        System.out.println(BankAccount.getTotalMoney());

    }
}
