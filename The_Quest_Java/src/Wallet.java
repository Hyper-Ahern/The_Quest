public class Wallet extends MoneyHolders {

  public boolean buy (Items item) {
    int balance = this.getBalance();
    int cost = item.getCost();
    if (balance >= cost) {
      this.setBalance(balance - cost);
      return true;
    }
    System.out.println("You don't have enough money.");
    return false;
  }

  public void sell(Items item) {
    int value = (int) (item.getCost() * 0.75);
    if (this.getCapacity() <= this.getBalance() + value) {
      this.setBalance(this.getCapacity());
      return;
    }
    this.setBalance(this.getBalance() + value);
  }
}
