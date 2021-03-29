public abstract class Weapons extends Equipment {

  private int damage;
  private String damageType;

  public int getDamage() {
    return damage;
  }

  public String getDamageType() {
    return damageType;
  }

  public void setDamage(int damage) {
    this.damage = damage;
  }

  public void setDamageType(String damageType) {
    this.damageType = damageType;
  }

  public void showStats() {
    System.out.println("Item: " + this.getName());
    System.out.println("Durability: " + this.getDurability());
    System.out.println("Damage: " + this.getDamage());
    System.out.println("Damage Type: " + this.getDamageType());
    System.out.println();
  }
}
