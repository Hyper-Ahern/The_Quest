public abstract class Armor extends Equipment {

  private int defence;

  public void setDefence(int def) {
    this.defence = def;
  }

  public int getDefence() {
    return defence;
  }

  public void showStats() {
    super.showStats();
    System.out.println("Defense: " + this.getDefence());
  }

}
