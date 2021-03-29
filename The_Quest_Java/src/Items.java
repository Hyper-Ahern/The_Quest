public abstract class Items implements ItemStats {

  private String name;
  protected int size = 1;
  private int cost;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getSize() {
    return size;
  }

  public int getCost() {
    return cost;
  }

  public void setCost(int cost) {
    this.cost = cost;
  }

  public void showStats() {
    System.out.println("Name: " + this.getName());
  }


}
