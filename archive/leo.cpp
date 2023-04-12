#include <iostream>
#include <windows.h>
using namespace std;

// todo change cls to cls
// change system("pause") to system("pause")

class Project
{
public:
	void introTab();
	void exitTab();
	void initialMenu();
	void LINdetails();
	void LANdetails();

private:
	int i, j, k, l, z, m;
	int houseType, noOfBedroom, noOfBathroom, noOfBedroom2, noOfBathroom2, floorAreaKitchen, floorAreaKitchen2;
	int floorAreaBed[5], floorAreaBath[5], floorAreaBed2[5], floorAreaBath2[5], houseNo[10];
	int noOfHouses;

	double houseTypes[10], noOfBedrooms[10], noOfBathrooms[10];
	double paintCost[10], flooringCost[10], laborCostMin[10], laborCostMax[10], houseSubTotalsMin[10], houseSubTotalsMax[10];
	double totalPaintCost = 0, totalFlooringCost = 0, totalLaborCostMin = 0, totalLaborCostMax = 0, totalMin = 0, totalMax = 0;
};

void Project::introTab()
{
	system("color B");
	cout << "\n\n  HOUSING PROJECT BUDGET PROPOSAL SYSTEM                                 ";
	cout << "\n   ________________________________________________________________________";
	cout << "\n    ______________________________________________________________________";
	cout << "\n     ____________________________________________________________________";
	cout << "\n\n     Name       :                                      Tyron Kevin Silva" << endl;
	cout << "                                                 Jash Gabriella Villegas" << endl;
	cout << "\n\n     Class      :                                                 BS-CS";
	cout << "\n\n     Section    :                                                   C2A";
	cout << "\n\n     Instructor :                                     Sir Franze Garcia";
	cout << "\n\n     School     :                                       De LaSalle Lipa";
	cout << "\n     ____________________________________________________________________";
	cout << "\n    ______________________________________________________________________";
	cout << "\n   ________________________________________________________________________\n\n\n";

	system("pause");
}

void Project::exitTab()
{
	system("color B");
	cout << "\t\t THANK YOU FOR USING THIS SOFTWARE" << endl;

	cout << "\n\n";
	cout << "\t   GROUP MEMBERS(DEVELOPERS)";
	cout << "\n\n";
	cout << "\t   NAME                                \n\n";
	cout << "\t   1. Tyron Kevin Silva                   \n\n";
	cout << "\t   2. Jash Gabriella Villegas                  \n\n";
	cout << "\n\n";
	cout << "\t\t\t\t\t\t\t\t\t   SUBMITED TO:   Sir Franze Garcia\n";
	cout << "\t\t\t\t\t\t\t\t\t   SUBMITED DATE: 12/08/2022 ";

	cout << "\n\n";
}

void Project::initialMenu()
{

	int houseType;
	cout << "=====CREATE HOUSE PROJECT PROPOSAL=====\n"
			 << endl;
	cout << "Desired number of Houses: ";
	cin >> noOfHouses;
	system("cls");

	for (m = 1; m <= noOfHouses; m++)
	{
	a:
		system("cls");
		cout << "=====HOUSE PROJECT INFORMATION=====" << endl;
		cout << "House: " << m << endl;

		cout << "\n[1] LIN HOUSE TYPE: One Story House (180 sqm)" << endl;
		cout << "[2] LAN HOUSE TYPE: Two Story House (250 sqm)" << endl;
		cout << "\nDesired House Type [1/2]: ";

		cin >> houseType;
		if (houseType < 1 || houseType > 2)
		{
			system("cls");
			cout << "Wrong Input! Choose between [1/2] \n"
					 << endl;
			system("pause");
			system("cls");
			goto a;
		}

		switch (houseType)
		{
		case 1:
			houseTypes[m] = 1;
			LINdetails();
			break;

		case 2:
			houseTypes[m] = 2;
			LANdetails();
			break;
		}
	}

	for (i = 1; i < m; i++)
	{
		system("cls");
		cout << "=====HOUSE PROJECT INFORMATION=====" << endl;
		cout << "House : " << i << endl;
		cout << "HOUSE TYPE: " << endl;

		if (houseTypes[i] == 1)
		{
			cout << "\tLIN HOUSE TYPE: One Story House (180 sqm) " << endl;
		}
		else
		{
			cout << "\tLAN HOUSE TYPE: Two Story House (250 sqm) " << endl;
		}

		cout << "\nNumber of Bedroom: " << noOfBedrooms[i] << endl;
		cout << "\nNumber of Bathroom: " << noOfBathrooms[i] << endl;
		cout << "\nNumber of Kitchen: 1 " << endl;
		cout << "\n===== PROJECTED BUDGET =====\n";
		cout << "\nExpenses of House " << i << endl;
		cout << "   Paint Cost (PHP): " << paintCost[i] << endl;
		cout << "   Flooring Cost (PHP): " << flooringCost[i] << endl;
		cout << "   Labor Cost (PHP): " << laborCostMin[i] << " to " << laborCostMax[i] << endl;
		cout << "   Subtotal for House " << i << ": " << houseSubTotalsMin[i] << " to " << houseSubTotalsMax[i] << endl;

		totalPaintCost += paintCost[i];
		totalFlooringCost += flooringCost[i];
		totalLaborCostMin += laborCostMin[i];
		totalLaborCostMax += laborCostMax[i];
		totalMin += houseSubTotalsMin[i];
		totalMax += houseSubTotalsMax[i];
		system("pause");
	}

	system("cls");
	cout << "=====HOUSE PROJECT INFORMATION=====" << endl;
	cout << "Houses : " << i - 1 << endl;
	cout << "\nExpenses of Project " << endl;
	cout << "   Total Paint Cost (PHP): " << totalPaintCost << endl;
	cout << "   Total Flooring Cost (PHP): " << totalFlooringCost << endl;
	cout << "   Total Labor Cost (PHP): " << totalLaborCostMin << " to " << totalLaborCostMax << endl;
	cout << "   Total for Project: " << totalMin << " to " << totalMax << endl;
	system("pause");
}

void Project::LINdetails()
{
	for (z = 1; z <= 1; z++)
	{
	b:
		cout << "\n=====LIN HOUSE TYPE=====" << endl;
		cout << "\nNumber of Bedroom [1-4]: ";
		cin >> noOfBedroom;
		// input validation
		if (noOfBedroom < 1 || noOfBedroom > 4)
		{
			system("cls");
			cout << "Wrong Input! Choose between [1-4] \n"
					 << endl;
			system("pause");
			system("cls");
			goto b;
		}
		for (i = 1; i <= noOfBedroom; i++)
		{
			cout << "   Floor Area of Bedroom " << i << " (sqm): ";
			cin >> floorAreaBed[i];
		}
	c:
		cout << "\nNumber of Bathroom [1-2]: ";
		cin >> noOfBathroom;
		if (noOfBathroom < 1 || noOfBathroom > 2)
		{
			cout << "Wrong Input! Choose between [1-2] \n"
					 << endl;
			system("pause");
			system("cls");
			goto c;
		}

		for (j = 1; j <= noOfBathroom; j++)
		{
			cout << "   Floor Area of Bathroom " << j << " (sqm): ";
			cin >> floorAreaBath[j];
		}

		cout << "\nNumber of Kitchen: 1" << endl;
		cout << "   Floor are of Kitchen (sqm): ";
		cin >> floorAreaKitchen;

		// Display Lin Dettails
		system("cls");
		cout << "=====HOUSE INFORMATION=====" << endl;
		cout << "House : " << m << endl;
		cout << "\nHOUSE TYPE: " << endl;
		cout << "\tLIN HOUSE TYPE: One Story House (180 sqm) " << endl;

		cout << "\nNumber of Bedroom: " << noOfBedroom << endl;
		for (i = 1; i <= noOfBedroom; i++)
		{
			cout << "  Floor Area of Bedroom " << i << ": " << floorAreaBed[i] << endl;
		}

		cout << "\nNumber of Bathroom: " << noOfBathroom << endl;
		for (j = 1; j <= noOfBathroom; j++)
		{
			cout << "  Floor Area of Bathroom " << j << ": " << floorAreaBath[j] << endl;
		}
		cout << "\nNumber of Kitchen: 1 " << endl;
		cout << "  Floor Area of Kitchen " << floorAreaKitchen << endl;
		cout << "\n===== PROJECTED BUDGET =====\n";

		system("pause");

		// calculate
		double rate;

		// costs
		double tempPaintCost = 0;
		double tempFlooringCost = 0;
		double tempLaborCostMin = 0;
		double tempLaborCostMax = 0;

		// painting
		// bedrooms
		for (i = 1; i <= noOfBedroom; i++)
		{
			rate = 125;
			if (floorAreaBed[i] > 30 && floorAreaBed[i] < 41)
			{
				rate = 175.25;
			}
			else if (floorAreaBed[i] > 40)
			{
				rate = 205.50;
			}
			tempPaintCost += rate * floorAreaBed[i];
		}

		// kitchen
		if (floorAreaKitchen <= 50)
		{
			tempPaintCost += 12500;
		}
		else
		{
			tempPaintCost += 12500 + ((floorAreaKitchen - 50) * 75.45); // 12500 + excess is 75.45 per sqm
		}

		// bathroom
		tempPaintCost += 6550 * noOfBathroom;

		// flooring
		tempFlooringCost += 123450; // base price for lin

		// bedroom
		if (noOfBedroom > 2)
		{
			tempFlooringCost += (noOfBedroom - 2) * 8500;
		}

		// bathroom
		if (noOfBathroom > 1)
		{
			tempFlooringCost += (noOfBedroom - 1) * 4750;
		}

		// labor
		// painting
		tempLaborCostMin += 5 * 5 * 650;	 // 5 workers for 5 days 650 per day
		tempLaborCostMax += 10 * 10 * 650; // 10 workers for 10 days 650 per day

		// floor
		tempLaborCostMin += 10 * 7 * 550;	 // 10 workers for 7 days 550 per day
		tempLaborCostMax += 15 * 15 * 650; // 15 workers for 15 days 550 per day

		noOfBedrooms[m] = noOfBedroom;
		noOfBathrooms[m] = noOfBathroom;
		paintCost[m] = tempPaintCost;
		flooringCost[m] = tempFlooringCost;
		laborCostMin[m] = tempLaborCostMin;
		laborCostMax[m] = tempLaborCostMax;

		double houseSubtotalMin = tempPaintCost + tempFlooringCost + tempLaborCostMin;
		double houseSubtotalMax = tempPaintCost + tempFlooringCost + tempLaborCostMax;

		houseSubTotalsMin[m] = houseSubtotalMin;
		houseSubTotalsMax[m] = houseSubtotalMax;

		cout << "\nExpenses of House " << m << endl;
		cout << "   Paint Cost (PHP): " << tempPaintCost << endl;
		cout << "   Flooring Cost (PHP): " << tempFlooringCost << endl;
		cout << "   Labor Cost (PHP): " << tempLaborCostMin << " to " << tempLaborCostMax << endl;
		cout << "   Subtotal for House " << m << ": " << houseSubtotalMin << " to " << houseSubtotalMax << endl;
		system("pause");
	}
}

void Project::LANdetails()
{
	for (z = 1; z <= 1; z++)
	{
	d:
		cout << "\n=====LAN HOUSE TYPE=====" << endl;
		cout << "\nNumber of Bedroom [1-5]: ";
		cin >> noOfBedroom2;
		if (noOfBedroom2 < 1 || noOfBedroom2 > 5)
		{
			system("cls");
			cout << "Wrong Input! Choose between [1-5] \n"
					 << endl;
			system("pause");
			system("cls");
			goto d;
		}
		for (k = 1; k <= noOfBedroom2; k++)
		{
			cout << "   Floor Area of Bedroom " << k << " (sqm): ";
			cin >> floorAreaBed2[k];
		}
	e:
		cout << "\nNumber of Bathroom [1-3]: ";
		cin >> noOfBathroom2;
		if (noOfBathroom2 < 1 || noOfBathroom2 > 3)
		{
			system("cls");
			cout << "Wrong Input! Choose between [1-3] \n"
					 << endl;
			system("pause");
			system("cls");
			goto e;
		}
		for (l = 1; l <= noOfBathroom2; l++)
		{
			cout << "   Floor Area of Bathroom " << l << " (sqm): ";
			cin >> floorAreaBath2[l];
		}

		cout << "\nNumber of Kitchen: 1" << endl;
		cout << "   Floor area of Kitchen (sqm): ";
		cin >> floorAreaKitchen2;

		// Display LAN Details
		system("cls");
		cout << "House : " << m << endl;
		cout << "=====HOUSE INFORMATION=====" << endl;
		cout << "\nHOUSE TYPE: " << endl;
		cout << "\tLAN HOUSE TYPE: Two Story House (250 sqm) " << endl;

		cout << "\nNumber of Bedroom: " << noOfBedroom2 << endl;
		for (k = 1; k <= noOfBedroom2; k++)
		{
			cout << "  Floor Area of Bedroom " << k << ": " << floorAreaBed2[k] << endl;
		}

		cout << "\nNumber of Bathroom: " << noOfBathroom2 << endl;
		for (l = 1; l <= noOfBathroom2; l++)
		{
			cout << "  Floor Area of Bathroom " << l << ": " << floorAreaBath2[l] << endl;
		}

		cout << "\nNumber of Kitchen: 1 " << endl;
		cout << "  Floor Area of Kitchen "
				 << ": " << floorAreaKitchen2 << endl;
		cout << "\n===== PROJECTED BUDGET =====\n";

		system("pause");

		// calculate
		double rate;

		// costs
		double tempPaintCost = 0;
		double tempFlooringCost = 0;
		double tempLaborCostMin = 0;
		double tempLaborCostMax = 0;

		// painting
		// bedrooms
		for (i = 1; i <= noOfBedroom2; i++)
		{
			rate = 125;
			if (floorAreaBed2[i] > 30 && floorAreaBed2[i] < 41)
			{
				rate = 175.25;
			}
			else if (floorAreaBed2[i] > 40)
			{
				rate = 205.50;
			}
			tempPaintCost += rate * floorAreaBed2[i];
		}

		// kitchen
		if (floorAreaKitchen2 <= 50)
		{
			tempPaintCost += 12500;
		}
		else
		{
			tempPaintCost += 12500 + ((floorAreaKitchen2 - 50) * 75.45); // 12500 + excess is 75.45 per sqm
		}

		// bathroom
		tempPaintCost += 6550 * noOfBathroom;

		// flooring
		tempFlooringCost += 180500; // base price for lan

		// bedroom
		if (noOfBedroom > 2)
		{
			tempFlooringCost += (noOfBedroom - 2) * 8500;
		}

		// bathroom
		if (noOfBathroom > 1)
		{
			tempFlooringCost += (noOfBedroom - 1) * 4750;
		}

		// labor
		// painting
		tempLaborCostMin += 10 * 7 * 650;	 // 10 workers for 7 days 650 per day
		tempLaborCostMax += 15 * 14 * 650; // 15 workers for 14 days 650 per day

		// floor
		tempLaborCostMin += 10 * 7 * 550;	 // 10 workers for 7 days 550 per day
		tempLaborCostMax += 15 * 15 * 650; // 15 workers for 15 days 550 per day

		noOfBedrooms[m] = noOfBedroom2;
		noOfBathrooms[m] = noOfBathroom2;
		paintCost[m] = tempPaintCost;
		flooringCost[m] = tempFlooringCost;
		laborCostMin[m] = tempLaborCostMin;
		laborCostMax[m] = tempLaborCostMax;

		double houseSubtotalMin = tempPaintCost + tempFlooringCost + tempLaborCostMin;
		double houseSubtotalMax = tempPaintCost + tempFlooringCost + tempLaborCostMax;

		houseSubTotalsMin[m] = houseSubtotalMin;
		houseSubTotalsMax[m] = houseSubtotalMax;

		cout << "\nExpenses of House " << m << endl;
		cout << "   Paint Cost (PHP): " << tempPaintCost << endl;
		cout << "   Flooring Cost (PHP): " << tempFlooringCost << endl;
		cout << "   Labor Cost (PHP): " << tempLaborCostMin << " to " << tempLaborCostMax << endl;
		cout << "   Subtotal for House " << m << ": " << houseSubtotalMin << " to " << houseSubtotalMax << endl;
		system("pause");
	}
}

int main()
{
	Project proposal;
	proposal.introTab();
	int again;
	int type;
	system("cls");

	do
	{
		system("cls");
		cout << "\t\t\t\t=================MAIN MENU================\n\n"
				 << endl;
		Sleep(100);
		cout << "\t\t\t\t[1] CREATE HOUSE PROJECT PROPOSAL\n\n"
				 << endl;
		Sleep(100);
		cout << "\t\t\t\t[2] EXIT\n\n"
				 << endl;
		Sleep(500);
		cout << "\t\t\t\t=========================================" << endl;
		cout << "\n";
		cout << "\t\t\t\tEnter Choice: ";
		cin >> type;
		cin.ignore();
		system("cls");

		switch (type)
		{
		case 1:
			proposal.initialMenu();
			break;

		case 2:
			system("cls");
			proposal.exitTab();
			exit(0);
			break;
		default:
			cout << "Invalid Input." << endl;
			exit(0);
			break;
		}

	} while (again != 2);

	return 0;
}
