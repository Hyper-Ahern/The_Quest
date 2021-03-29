public class KiteShield extends Shields implements ItemStats {

  private final int DEFENCE = 12;
  private final int BLOCK = 15;
  private int durability = 12;
  private String name = "Kite Shield";


  public KiteShield() {
    this.setDurability(durability);
    this.setBlock(BLOCK);
    this.setDefence(DEFENCE);
    this.setName(name);
  }

  public void showStats() {
    System.out.println("Item: " + this.getName());
    System.out.println("Durability: " + this.getDurability());
    System.out.println("Block: " + this.getBlock());
    System.out.println("Defence: " + this.getDefence());
  }

}
