import java.util.ArrayList;

public class Inventory {
  ArrayList<Items> inventory;
  private int capacity;

  public Inventory(int capacity) {
    inventory = new ArrayList<>();
    this.capacity = capacity;
  }

  public int getCapacity() {
    return capacity;
  }

  public void setCapacity(int capacity) {
    this.capacity = capacity;
  }

  //If the inventory has available space add the item and return true, increments capacity
  public boolean add(Items item) {
    int itemSize = item.getSize();
    if (capacity >= capacity + itemSize) {
      inventory.add(item);
      capacity += itemSize;
      return true;
    }
    System.out.println("Your inventory is full!");
    return false;
  }

  //if requested item is in inventory will remove that item and return true, decrements capacity
  public boolean remove(Items item) {
    for (Items i : inventory) {
      if (i.equals(item)) {
        inventory.remove(item);
        capacity -= item.getSize();
        return true;
      }
    }
    return false;
  }
}
