public class KiteShield extends Shields {

  private String name = "Kite Shield";
  private int durability = 12;
  private final int DEFENCE = 12;
  private final int BLOCK = 15;


  public KiteShield() {
    this.setName(name);
    this.setDurability(durability);
    this.setDefence(DEFENCE);
    this.setBlock(BLOCK);
    this.setCost(5);
  }



}
