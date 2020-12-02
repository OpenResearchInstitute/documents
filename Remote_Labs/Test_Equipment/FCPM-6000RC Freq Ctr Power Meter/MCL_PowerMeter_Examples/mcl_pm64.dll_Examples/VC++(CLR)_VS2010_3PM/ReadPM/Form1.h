#pragma once


namespace ReadPM {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for Form1
	///
	/// WARNING: If you change the name of this class, you will need to change the
	///          'Resource File Name' property for the managed resource compiler tool
	///          associated with all .resx files this class depends on.  Otherwise,
	///          the designers will not be able to interact properly with localized
	///          resources associated with this form.
	/// </summary>
	public ref class Form1 : public System::Windows::Forms::Form
	{
	public:
		
		Form1(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~Form1()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Label^  label1;
	protected: 
	private: System::Windows::Forms::TextBox^  textBox1;
	private: System::Windows::Forms::Label^  label2;
	private: System::Windows::Forms::Label^  label3;
	private: System::Windows::Forms::Label^  label4;
	private: System::Windows::Forms::Button^  button1;
	private: System::Windows::Forms::Label^  label5;
	private: System::Windows::Forms::Label^  label6;


	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->label4 = (gcnew System::Windows::Forms::Label());
			this->button1 = (gcnew System::Windows::Forms::Button());
			this->label5 = (gcnew System::Windows::Forms::Label());
			this->label6 = (gcnew System::Windows::Forms::Label());
			this->SuspendLayout();
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->Location = System::Drawing::Point(65, 56);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(62, 13);
			this->label1->TabIndex = 0;
			this->label1->Text = L"Freq (MHz):";
			// 
			// textBox1
			// 
			this->textBox1->Location = System::Drawing::Point(68, 72);
			this->textBox1->Name = L"textBox1";
			this->textBox1->Size = System::Drawing::Size(147, 20);
			this->textBox1->TabIndex = 1;
			this->textBox1->Text = L"1000";
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->Location = System::Drawing::Point(71, 134);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(69, 13);
			this->label2->TabIndex = 2;
			this->label2->Text = L"Read Result:";
			// 
			// label3
			// 
			this->label3->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 26.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point, 
				static_cast<System::Byte>(177)));
			this->label3->Location = System::Drawing::Point(73, 163);
			this->label3->Name = L"label3";
			this->label3->Size = System::Drawing::Size(128, 59);
			this->label3->TabIndex = 3;
			this->label3->Text = L"-99.99";
			// 
			// label4
			// 
			this->label4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 26.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point, 
				static_cast<System::Byte>(177)));
			this->label4->Location = System::Drawing::Point(559, 163);
			this->label4->Name = L"label4";
			this->label4->Size = System::Drawing::Size(103, 43);
			this->label4->TabIndex = 4;
			this->label4->Text = L"dBm.";
			// 
			// button1
			// 
			this->button1->Location = System::Drawing::Point(80, 237);
			this->button1->Name = L"button1";
			this->button1->Size = System::Drawing::Size(149, 62);
			this->button1->TabIndex = 5;
			this->button1->Text = L"Read Once...";
			this->button1->UseVisualStyleBackColor = true;
			this->button1->Click += gcnew System::EventHandler(this, &Form1::button1_Click);
			// 
			// label5
			// 
			this->label5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 26.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point, 
				static_cast<System::Byte>(177)));
			this->label5->Location = System::Drawing::Point(225, 163);
			this->label5->Name = L"label5";
			this->label5->Size = System::Drawing::Size(128, 59);
			this->label5->TabIndex = 6;
			this->label5->Text = L"-99.99";
			// 
			// label6
			// 
			this->label6->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 26.25F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point, 
				static_cast<System::Byte>(177)));
			this->label6->Location = System::Drawing::Point(379, 163);
			this->label6->Name = L"label6";
			this->label6->Size = System::Drawing::Size(128, 59);
			this->label6->TabIndex = 7;
			this->label6->Text = L"-99.99";
			// 
			// Form1
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(684, 386);
			this->Controls->Add(this->label6);
			this->Controls->Add(this->label5);
			this->Controls->Add(this->button1);
			this->Controls->Add(this->label4);
			this->Controls->Add(this->label3);
			this->Controls->Add(this->label2);
			this->Controls->Add(this->textBox1);
			this->Controls->Add(this->label1);
			this->Name = L"Form1";
			this->Text = L"Form1";
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void button1_Click(System::Object^  sender, System::EventArgs^  e) {
 mcl_pm64::usb_pm ^pmR = gcnew mcl_pm64::usb_pm();
 mcl_pm64::usb_pm ^pmF = gcnew mcl_pm64::usb_pm();
 mcl_pm64::usb_pm ^pmG = gcnew mcl_pm64::usb_pm();
 short Status = 0;
 System::String ^SN1 = "1003010042"; //if more then 1 sensor connected to the computer than the Serial Number of the sensor should provide
 System::String ^SN2 = "1001260005";
 System::String ^SN3 = "1004060009";
 float ReadResult = 0;
 Status = pmR->Open_Sensor(SN1);  // create a Connection to the sensor
 Status = pmF->Open_Sensor(SN2);
 Status = pmG->Open_Sensor(SN3);
  System::String ^FREQ_STR;
  FREQ_STR=textBox1->Text;

 pmR->Freq = System::Convert::ToDouble(FREQ_STR);      // Set the Frequency cal factor in MHz
 pmF->Freq = System::Convert::ToDouble(FREQ_STR); 
 pmG->Freq = System::Convert::ToDouble(FREQ_STR);
 ReadResult = pmR->ReadPower(); // read the power in dbm
 label3->Text=ReadResult.ToString();
 label3->Refresh();  
 ReadResult = pmF->ReadPower(); // read the power in dbm
 label5->Text=ReadResult.ToString();
 label5->Refresh();  
 ReadResult = pmG->ReadPower(); // read the power in dbm
 label6->Text=ReadResult.ToString();
 label6->Refresh();  

 pmF->Close_Sensor();  
 pmR->Close_Sensor();   
 pmG->Close_Sensor();   	
			 }

};
}

