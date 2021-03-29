public abstract class Items {

  private String name;
  private int durability;

  public void setDurability (int dur) {
    this.durability = dur;
  }

  public int getDurability() {
    return durability;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }
}
