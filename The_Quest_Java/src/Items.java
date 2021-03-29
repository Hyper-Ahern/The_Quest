public abstract class Items implements ItemStats {

  private String name;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void showStats() {
    System.out.println("Name: " + this.getName());
  }
}
