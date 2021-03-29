public abstract class Shields extends Armor {

  private int block;

  public int getBlock() {
    return block;
  }

  public void setBlock(int block ) {
    this.block = block;
  }

  public void showStats() {
    super.showStats();
    System.out.println("Block: " + this.getBlock() + "\n");
  }
}
