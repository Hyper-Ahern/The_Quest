public class BroadSword extends Sword {

//  private final String name = "Broad Sword";
  private final int damage = 5;
  private final int durability = 10;

  public BroadSword() {
    this.setDamage(damage);
    this.setDurability(durability);
    this.setName("Broad Sword");
    this.setDamageType(damageType);
    this.setCost(5);
  }
}
