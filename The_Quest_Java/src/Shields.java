public abstract class Shields extends Armor {

  private int block;

  public int getBlock() {
    return block;
  }

  public void setBlock(int block ) {
    this.block = block;
  }

  public void showStats() {
    System.out.println("Item: " + this.getName());
    System.out.println("Durability: " + this.getDurability());
    System.out.println("Block: " + this.getBlock());
    System.out.println("Defence: " + this.getDefence()+ "\n");
  }
}
